
import pandas as pd
import numpy as np
import re
import os
import json
import formulae as f


# Build dataframe
str_cols = ["loan_id", "product"]
date_cols = ["origination_date", "reversion_date"]
nums_cols = ["rate_term", "loan_amount",
             "initial_rate", "term", "interest_only_amount", "upfront_fees", "upfront_costs", "adjust Nov-21"]


class Mappings:
    def __init__(self):
        self.data = { # Initialise the empty mappings dictionary
            "loan_id": None,
            "product": None,
            "origination_date": None,
            "reversion_date": None,
            "loan_amount": None,
            "initial_rate": None,
            "reversion_rate": None,
            "term": None,
            "interest_only_amount": None,
            "upfront_fees": None,
            "upfront_costs": None,
            "entity_eir": None
        }


    def update(self, internal, external, allowable): # used to update the mappings
        # Check if external label is contained within hte allowable list
        if external in allowable:
            self.data[internal] = external
        else:
            raise KeyError(f"External label '{external}' does not exist in "
                           f"the allowable set of values.")


    def new(self, df): # Enables user to enter new column label mappings via command line
        cols = df.columns
        print(cols) # Control

        for key in self.data:
            # Keep asking for correct column names
            while True:
                try:
                    ext = input(f"Type external column name giving '{key}'."
                                "\n>>> ")
                    self.update(key, ext, list(cols))
                    break
                except KeyError as e:
                    print(f"KeyError: {e}"
                          "\nCheck for typos."
                          "\nAvailable columns are:\n"
                          f"{list(cols)}")


    def save(self, file="setup", path="settings"): # Saves the mappings dict to file as .json
        if file[-5:] != ".json":
            file += ".json"
        with open(os.path.join(path, file), "w") as file:
            json.dump(self.data, file)


    def load(self, file="setup", path="settings"): # Loads the mappings .json to the objects internal self.data
        if file[-5:] != ".json":
            file += ".json"
        with open(os.path.join(path, file), 'r') as file:
            self.data = json.load(file)


    def reserve(self): # Reverses outputs of self.data dict
        return {self.data[key]: key for key in self.data}


def output(df, path="./outputs", file="output"): # Function used to save .csv output
    if not os.path.isdir(path):
        os.makedirs(path)

    if ".csv" in file: # Remove file extension if included
        file = file.replace(".csv", "")
    full_path = os.path.join(path, f"{file}.csv")

    while True:
        try:
            df.to_csv(full_path, sep="|", index=False)
            print(f"{file} data issues saved to " # Update user
                  f"'{full_path}'.")
            break
        except PermissionError: # If file is open, request to close or rename
            rename = input(f"'{full_path}' is open. To Proceed close and press <Enter> or type a mew filename")

            if rename.strip() == "":
                pass
            elif ".csv" in rename.strip():
                full_path = os.path.join(path, rename) # Merger path and file
            else:
                full_path = os.path.join(path, rename+".csv")


def format_loanbook(loanbook, mapping, conv_full_term=False, verbose=True): # Formats loanbook or EIR processing
    loanbook.rename({col: mapping[col] for col in loanbook.columns
                     if col in mapping},
                    axis=1, inplace=True)

    if conv_full_term:
        def conv_rates(rate_term, term): # Define numeric type checking function
            if str(rate_term).isnumeric():
                return rate_term
            else:
                return float(term) / 12

        loanbook["rate_term"] = list(map( # Apply numeric checking function to the dataframe
            conv_rates, loanbook["rate_term"], loanbook["term"]
        ))

    for col in loanbook.columns: # Changing data type from external to internal
        try:
            if col in str_cols:
                loanbook[col] = pd.Series(
                    loanbook[col].astype(str), index=loanbook.index)
            elif col in date_cols:
                loanbook[col] = pd.Series(
                    pd.to_datetime(loanbook[col]), index=loanbook.index)
            elif col in nums_cols:
                loanbook[col] = pd.Series(
                    pd.to_numeric(loanbook[col]), index=loanbook.index)
            else:
                if verbose:
                    print(f"WARNING: '{col}' datatype not set. This column "
                          "will default to string.")
                loanbook[col] = pd.Series(
                    loanbook[col].astype(str), index=loanbook.index)
        except ValueError as e:
            raise ValueError(f"ValueError for column '{col}':" + "\n" + f"{e}")

    return loanbook


def calc_loanbook(loanbook, verbose=True):
    loanbook["total_repayment"] = pd.Series(
        loanbook["loan_amount"] - loanbook["interest_only_amount"],
        index=loanbook.index)

    loanbook["monthly_repay"] = pd.Series(-np.pmt( # Monthly repayed amount
        loanbook["initial_rate"]/12,
        loanbook["term"],
        loanbook["total_repayment"]),
            index=loanbook.index)

    loanbook["monthly_repay_io"] = pd.Series( # Initial monthly payment IO = interest ate * IO amt / months in year
        (loanbook["initial_rate"]*loanbook["interest_only_amount"])/12,
        index=loanbook.index)

    loanbook["monthly_repay_io_reversion"] = pd.Series(
        (loanbook["reversion_rate"]*loanbook["interest_only_amount"])/12,
        index=loanbook.index)

    balance_on_reversion = []

    for i in range(len(loanbook)):
        cumprinc = f.princcum(
            loanbook["initial_rate"].iloc[i] / 12,
            loanbook["term"].iloc[i],
            loanbook["total_repayment"].iloc[i],
            int(loanbook["rate_term"].iloc[i]) * 12,
        )
        balance_on_reversion.append(
            loanbook["total_repayment"].iloc[i] - cumprinc)

    loanbook["reversion_balance"] = pd.Series(balance_on_reversion,
                                              index=loanbook.index)

    monthly_repay_reversion = []
    dtype_warning = 0 # Initialise data-type issue counter
    # Iterate through each loan and check if data is correct. If true perform calculations
    for i in range(len(loanbook)):
        if loanbook["total_repayment"].iloc[i] != 0:
            pmt = (-np.pmt(
                loanbook["reversion_rate"].iloc[i] / 12,
                loanbook["term"].iloc[i] - (
                int(loanbook["rate_term"].iloc[i])*12),
                loanbook["reversion_balance"].iloc[i]))
            monthly_repay_reversion.append(pmt)
        else:
            dtype_warning += 1
            monthly_repay_reversion.append(0)

    # Control to inform user if rows could not be converted
    if dtype_warning != 0 and verbose:
        print(f"Warning: {dtype_warning} 'Monthly Repay Reversion' rows "
              "can not be calculated as the 'total_repayment' value is 0. "
              "These 'monthly_repay_reversion' values have defaulted to 0.")
    loanbook['monthly_repay_reversion'] = pd.Series(monthly_repay_reversion,
                                                    index=loanbook.index)

    loanbook = adjust(loanbook)  # Formatting adjustment columns

    loanbook["upfront_costs"] = pd.Series(
        loanbook["upfront_costs"].fillna(0), index=loanbook.index)
    loanbook["upfront_fees"] = pd.Series(
        loanbook["upfront_fees"].fillna(0), index=loanbook.index)

    return loanbook


def format_array(array, mapping): # Rename columns o internal names using mapping dict
    array.rename({col: mapping[col] for col in array.columns
                  if col in mapping},
                 axis=1, inplace=True)

    for col in array.columns: # Convert from external dtype to internal
        if col in str_cols:
            array[col] = pd.Series(
                array[col].astype(str), index=array.index)
        else: # Assumes column CPR or ERC
            array[col] = pd.Series(
                pd.to_numeric(array[col]), index=array.index)

    # Format numeric columns headers to include only numbers
    array.rename({col: re.sub("\D", "", str(col)) for col in array.columns \
                  if col not in str_cols},
                 axis=1, inplace=True)

    # If empty replace with zero
    array = array.fillna(0)

    return array


def search_col(sheet, start, value, limit=200): # Searches a column in sheet for a specific value
    re_str = re.compile("[^a-zA-Z]") # Identifies all non-string values
    col = re_str.sub("", start) # Get a column
    re_int = re.compile("[^0-9]") # Identifies all non-integer values
    row = int(re_int.sub("", start)) # Get a row

    for _ in range(limit):
        if sheet[col+str(row)].value == value:
            return(col, row)
        row += 1
    raise KeyError(f"{value} not found in column {col} of workbook.")


def adjust(loanbook): # Reads dataframe and extracts adjustment columns
    ag8_cols = [x for x in loanbook.columns if "adjust" in x.lower()]

    for col in ag8_cols: # Randomly select number of products

        loanbook[col] = pd.Series(loanbook[col].filna(0),
                                  index=loanbook.index)

    return loanbook


def make_loans(volume): # Randomly generates loanbook in correspondence with CPR curves and ERC lookup
    loanbook = pd.DataFrame({"loan_id": range(volume)}) # Initialise loanbook data
    num_products = round(volume / np.random.randint(2, 5)) # Randomly select number of products
    products = [f"Product {i}" for i in range(num_products)] # Create list of product names
    raise ValueError("Function not build yet") # Create random origination dates within a range
