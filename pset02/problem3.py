monthlyInterestRate = annualInterestRate / 12.0

def minPayment(balance, annualInterestRate):
    '''
    function that uses bounds and bisection search to find the smallest monthly
     payment to the cent  needed in order pay
    off a credit card balance within 12 months.
    '''


    mbalance = balance
    lowerl = mbalance / 12
    upperl = (mbalance * (1 + monthlyInterestRate)**12) / 12.0

    while mbalance != 0:
        monthlyPayment = (lowerl + upperl) / 2
        mbalance = balance
        for month in range(0, 12):
            monthlyUnpaidbalance = mbalance - monthlyPayment
            mbalance = monthlyUnpaidbalance + (monthlyInterestRate * monthlyUnpaidbalance)
        if mbalance > 0:
            lowerl = monthlyPayment
        elif mbalance < 0:
            upperl = monthlyPayment
        mbalance = round(mbalance, 2)
    print("Lowest Payment:", round(monthlyPayment, 2))


minPayment(balance, annualInterestRate)
