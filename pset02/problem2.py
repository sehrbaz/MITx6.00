monthlyPayment = 10


def minPayment(balance, annualInterestRate, monthlyPayment):
    '''
    that calculates the minimum fixed monthly payment needed in order pay
    off a credit card balance within 12 months.
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    mbalance = balance

    for i in range(12):
        monthlyUnpaidbalance = mbalance - monthlyPayment
        mbalance = monthlyUnpaidbalance + (monthlyInterestRate * monthlyUnpaidbalance)
    if mbalance <= 0:
        print("Lowest Payment:", monthlyPayment)
    else:
        monthlyPayment += 10
        minPayment(balance, annualInterestRate, monthlyPayment)


minPayment(balance, annualInterestRate, monthlyPayment)

"""
Method 2: Iteration

def minPayment(balance, annualInterestRate):
    '''
    that calculates the minimum fixed monthly payment needed in order pay
    off a credit card balance within 12 months.
    '''

    mbalance = balance
    monthlyPayment = 10
    monthlyInterestRate = annualInterestRate / 12.0


    while mbalance > 0:
        for month in range(0, 12):
            monthlyUnpaidbalance = mbalance - monthlyPayment
            mbalance = monthlyUnpaidbalance + (monthlyInterestRate * monthlyUnpaidbalance)
        if mbalance > 0:
            monthlyPayment += 10
            mbalance = balance


    print(round(monthlyPayment, 2))

minPayment(balance, annualInterestRate)
"""
