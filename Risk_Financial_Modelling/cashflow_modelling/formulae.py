
import numpy as np

def princcum(rate, nper, loan_amount, period, when): # Calculates cumulative principal repaid between first month and n-month of the loan
    principal_paid = 0
    repay = -np.pmt(rate, nper, loan_amount, 0, when) # Calculate monthly repay

    if when == 1: # If repay is calculated at the start of the month, calculate first month now
        loan_amount -= repay
        principal_paid += repay
        period -= 1

    for i in range(period): # Iterate through each month in period
        month_interest = loan_amount * rate # Monthly interest
        paid_off = repay - month_interest
        principal_paid += paid_off # Cumulative amount paid
        loan_amount -= paid_off # Outstanding notional

    return principal_paid


# Scheduled payment calculation
def func_scheduled_payment(m, loan_amount, reversion, cpy_prev, ostmt, epmt_prev,
                          spmt_prev, monthly_repay_io, monthly_repay,
                          monthly_repay_reversion, monthly_repay_io_reversion):

    if m == 1: # IO - interest only. Scheduled payment calculation is applied to non-interest loans
        spmt = -monthly_repay_io - monthly_repay

    elif m == reversion - 1:
        spmt = -(monthly_repay_reversion +
                 monthly_repay_io_reversion) * \
                 (loan_amount - cpy_prev) / loan_amount

    else:
        if ostmt - epmt_prev != 0:
            spmt = (ostmt * spmt_prev) / (ostmt - epmt_prev)
        else:
            spmt = 0

    return spmt

v_scheduled_payment = np.vectorize(func_scheduled_payment) # Vectorised implementation of scheduled payment function


def cum_prepayment(cpy_prev, amount, cam, cpr, cpr_prev): # Calculates cumulative prepayment
    return cpy_prev + (amount + cam) * ((1 - cpr) -
                                        (1 - cpr_prev))


def func_early_repayment(ostmt, sint, spmt, cpy_prev, cpy): # Calculates early repayment
    # If cumulative prepayment this month is less than previous month + previous statement amount + current statement interest and scheduled payment, return previous - current cumulative prepayment amount
    # Otherwise early repayment is previous statement balance + current interest + current scheduled payment
    if (ostmt + sint + spmt + cpy_prev - cpy > 0):
        return cpy_prev - cpy
    else:
        return -(ostmt + sint + spmt)

v_early_repayment = np.vectorize(func_early_repayment) # Vectorised implementation of early repayment calculation


def cashflow_calc(prev_amount, prev_costs, prev_fees, prev_spmt, prev_epmt, erc, adjustments): # Calculates current cashflows
    return prev_amount + prev_costs - prev_fees + \
           prev_spmt + prev_epmt + erc + adjustments


