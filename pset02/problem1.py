month = 0


def remBalance(balance, annualInterestRate, monthlyPaymentRate, month):
    '''
    Function that calculate the credit card balance after one year if a person
    only pays the minimum monthly payment required by the credit card company
    each month.
    '''
    if month == 12:
        print(round(balance, 2))
    else:
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidbalance = balance - monthlyPayment
        balance = monthlyUnpaidbalance + (monthlyInterestRate * monthlyUnpaidbalance)
        month += 1
        remBalance(balance, annualInterestRate, monthlyPaymentRate, month)


remBalance(balance, annualInterestRate, monthlyPaymentRate, month)
