
import numpy as np
import pandas as pd
import os
import math
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import formulae as f
import data as d


def month_diff(x, y): # Difference in years * 12 + difference in months
    return (y.year - x.year) * 12 + y.month - x.month


def adjustment_month_diff(adjust_str, start_date): # Returns to relative month difference between adjustment date and start date
    adjust_dt = datetime.strptime(adjust_str.lower().replace('adjust', '').strip(),
                                  '%b-%y')
    return (adjust_dt.year - start_date.year) * 12 + \
        adjust_dt.month - start_date.month

def get_list(out, parameters): # Build a list containing pointers to all parameter arrays
    if out == "all":
        array_list = [
            parameters[key] for key in parameters
        ]
        parameter_list = [key for key in parameters]
    elif type(out) is list:
        array_list = [] # Initialise list of items to plot
        parameter_list = []
        for param in out:
            param = str(param).strip().lower()
            try: # If user has provided own list, iterate through it and where possible append a selected array to plot list
                array_list.append(parameters[param])
                parameter_list.append(param)
            except KeyError:
                print(f"Warning: '{param}' not added as "
                      "it does not exist. Check for typos and ensure name "
                      "matches to given options in documentation.\n"
                      "See 'get_list' in 'documentation/calculate' "
                      "for more information.")
    else:
        raise TypeError("'out' parameter must be either 'all' "
                        "to output all parameters, or a list "
                        "containing the names of parameters to "
                        "output.\n"
                        "See 'get_list' in 'documentation/calculate' "
                        "for more information.")
    return parameter_list, array_list

class Cashflow:
    # Class is used to control cashflow calculations. This contains calculations in addition to visualisation "plot" and result extraction "ouput" methods.
    # Before running this the Loanbooks, CPR Curves & ERC Lookup tables must have been formatted into correct formats using data script.
    def __init__(self, loanbook, erc_lookup):
        loans = loanbook.values.shape[0] # Get number of loans
        self.m_max = erc_lookup.shape[1] - 1 # Get maximum number of months

        self.products = loanbook["product"].str.strip().str.lower().value # Get list of all products
        self.erc_lookup = np.zeros((loans, self.m_max)) # Initialise empty array for new erc_lookup format

        for i in range(loans): # Build new erc_lookup array where rows match to rows in loanbook
            self.erc_lookup[i, :] = erc_lookup.drop(["product"], axis=1)[
                erc_lookup["product"].str.strip().str.lower() \
                == self.products[i]
            ].values

        self.early_repayment = np.zeros((loans, self.m_max)) # EPMT
        self.scheduled_payment = np.zeros((loans, self.m_max))  # SPMT
        self.statement_interest = np.zeros((loans, self.m_max))  # SINT
        self.cumulative_amortisation = np.zeros((loans, self.m_max))  # CM
        self.cumulative_payment = np.zeros((loans, self.m_max))  # CPY
        # self.net_present_value = np.zeros((loans, self.m_max))  # NPV
        self.profit_and_loss = np.zeros((loans, self.m_max))  # PLS
        self.cashflow = np.zeros((loans, self.m_max))  # Cashflow
        self.early_repayment_charge = np.zeros((loans, self.m_max))  # ERC
        self.statement_amount = np.zeros((loans, self.m_max))  # CSTMT / OSTMT

        self.statement_amount[:, 0] = loanbook["loan_amount"].values.T

        self.adjustments = np.zeros((loans, self.m_max)) # Initialise adjustments and interest ate arrays with zero
        self.rate = np.zeros((loans, self.m_max))
        adjust = []
        self.reversion = np.array(
            [month_diff(loanbook.iloc[i]['origination_date'],
                        loanbook.iloc[i]['reversion_date']) \
             for i in range(len(loanbook))]
            )

        for i in range(loans):
            loan = loanbook.iloc[i]
            adjust_amounts = [loan[col] for col in loan.index \
                              if "adjust" in col.lower()]
            
            if len(adjust_amounts) > 0: # If adjustments columns found add tuple to list
                adjust.extend(
                    [(i,
                      adjustment_month_diff(col, loan['origination_date']),
                      loan[col]) \
                     for col in loan.index if 'adjust' in col.lower()]
                )
            if self.reversion[i] < self.m_max: # Run through rate logic and additions to array
                init_rate = np.array( # Build initial rate array
                    [loan['initial_rate']] * self.reversion[i]
                )
                rev_rate = np.array( # Build reversion rate array
                    [loan['reversion_rate']] * (self.m_max - self.reversion[i])
                )
                self.rate[i, :] = np.concatenate((init_rate, rev_rate)) # Concatenate initial rate and reversion rates along column axis
            else:
                self.rate[i, :] = np.array(
                    [loanbook.iloc[i]['initial_rate']] * self.m_max
                ).T

        for i, month, amount in adjust: # Build adjustments array using adjust tuple list
            self.adjustments[i, month] = amount

        # Initialise initial costs, fees and loans amount arrays
        self.upfront_costs = np.zeros((loans, self.m_max))
        self.upfront_fees = np.zeros((loans, self.m_max))
        self.loan_amount = np.zeros((loans, self.m_max))

        # Initial costs/ fees only occur in month 0
        self.upfront_costs[:, 0] = loanbook['upfront_costs'].values.T
        self.upfront_fees[:, 0] = loanbook['upfront_fees'].values.T
        self.loan_amount[:, 0] = loanbook['loan_amount'].values.T

        # Keep loanbook in object for outputting to file in "output" method
        self.loanbook = loanbook

        # Define mapping parameters
        self.parameter_mapping = {
            'statement interest': self.statement_interest,
            'cumulative amortisation': self.cumulative_amortisation,
            'cumulative payment': self.cumulative_payment,
            'scheduled payment': self.scheduled_payment,
            'early repayment': self.early_repayment,
            'early repayment charge': self.early_repayment_charge,
            'cashflow': self.cashflow,
            'statement amount': self.statement_amount,
            'adjustments': self.adjustments,
            'interest rate': self.rate
            }

        # Check for calculated EIR column
        if "entity_eir" in loanbook:
            self.entity_eir = loanbook["entity_eir"].values
        else:
            print("Warning: No client/ entity calculated EUR column found")

    def calculated_Cashflow(self, cpr):
        self.cpr = np.zeros((self.erc_lookup.shape[0], self.m_max)) # Initialise empty array for new CPR curve format

        for i in range(len(self.products)): # Match CPR array to loanbook
            self.cpr[i, :] = cpr.drop(['product'], axis=1)[
                cpr['product'].str.strip().str.lower() \
                    == self.products[i]
                ].values

        for m in range(1, self.m_max): # Calculate values for a loans
            self.scheduled_payment[:, m] = f.v_scheduled_payment( # Use vectorised implementation of scheduled payment
                m,
                self.loan_amount[:, 0],
                self.reversion,
                self.cumulative_payment[:, m-1],
                self.statement_amount[:, m-1],
                self.early_repayment[:, m-1],
                self.scheduled_payment[:, m-1],
                self.loanbook['monthly_repay_io'].values,
                self.loanbook['monthly_repay'].values,
                self.loanbook['monthly_repay_reversion'].values,
                self.loanbook['monthly_repay_io_reversion'].values
                )

        # Calculating monthly interest
        self.statement_interest[:, m] = self.rate[:, m] * \
            self.statement_amount[:, m-1] / 12

        # Calculating total amortisation current month
        self.cumulative_amortisation[:, m] = \
            self.statement_interest[:, m - 1] + \
            self.scheduled_payment[:, m - 1] + \
            self.cumulative_amortisation[:, m - 1]

        # Calculating cumulative payment
        self.cumulative_payment[:, m] = f.cum_prepayment(
            self.cumulative_payment[:, m - 1],
            self.loan_amount[:, 0],
            self.cumulative_amortisation[:, m],
            self.cpr[:, m],
            self.cpr[:, m - 1]
        )

        # Calculating early repayment using vectorised implementation
        self.early_repayment[:, m] = f.v_early_repayment(
            self.statement_amount[:, m - 1],
            self.statement_interest[:, m],
            self.scheduled_payment[:, m],
            self.cumulative_payment[:, m - 1],
            self.cumulative_payment[:, m]
        )

        # ERC
        self.early_repayment_charge[:, m] = self.erc_lookup[:, m] * self.cashflow[:, m]

        #
        self.statement_amount[:, m] = \
            self.statement_amount[:, m - 1] + \
            self.statement_interest[:, m] + \
            self.scheduled_payment[:, m] + \
            self.early_repayment[:, m]


    def calculate_vals(self, period_start, period_end): # Calculating effective interest rate, net present value and profit and loss for cashflows
        self.eir = []
        self.npv = {}
        self.npv["calculated"] = []
        self.pl = []

        # Control checks if client/ entity EIR is valid
        if hasattr(self, 'entity_eir'):
            self.npv['entity'] = []
        else:
            print("Warning: Client/entity NPV will not be calculated.")
            self.npv['entity'] = [None] * len(self.loanbook)

        # Iterating from each loan and calculating values
        for i in range(self.cashflow.shape[0]):
            start = month_diff(
                    self.loanbook.iloc[i]['origination_date'],
                    period_start
                    )
            end = month_diff(
                    self.loanbook.iloc[i]['origination_date'],
                    period_end
                    )

            npv_cashflow = [0.] + self.cashflow[i, start:] # Filer cashflows occuring after the start period ir NPV
            self.eir.append(np.irr(self.cashflow[i, :-1])) # Calculating EIR
            self.npv["calculated"].append(-np.npv(self.eir[i], npv_cashflow)) # Calculating NPV
            if hasattr(self, "entity_eir"):
                self.npv["entity"].append(-np.npv(self.entity_eir[i], npv_cashflow))

            self.pl.append(sum(self.profit_and_loss[i, start:end])) # Calculating profit and loss per loan


    def plot(self, products='all', out='all',
             save=False, path="C:\Users\edgar\PycharmProjects\finance_modelling\cashflow_modelling",
             limit=30):

        # If directory do not exit make one
        if not os.path.isdir(path) and save:
            os.makedirs(path)

        parameter_list, plot_list = get_list(out, self.parameter_mapping)

        if products == "all":
            products = (self.loanbook["loan_id"].astype(str) +
                        self.loanbook["product"].astype(str)).values
            pass
        elif type(products) is list:
            products = [str(prod).strip().lower() for prod in products]
            idx = self.loanbook.index[self.loanbook["product"].str.strip().str.lower().isin(products)] # Looking for indexes of all rows that match to a product from list
            row_idx = np.array(idx)
            plot_list = [
                array[row_idx,]
            ]






































