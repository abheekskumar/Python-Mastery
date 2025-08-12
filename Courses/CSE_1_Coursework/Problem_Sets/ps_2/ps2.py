import math
def problem1(b,air,mpr):
    mir= air/12
    for i in range(12): # iterate for 12 times
        
        mmp = mpr*b # minimum balance to pay
        mub = b - mmp #monthly unpaid balance
        b = b-mmp# paid for that month
        b = b + mir*mub
    print(round(b,2))

def problem2(balance,air):
    b = balance
    mir = air/12 # monthly interest rate
    mfmp = 10 # minimum fixed montly payment
    while True: # loop increasing the multiplier on mfmp
        for i in range(12):# loop that creates the final balance
            mub = b - mfmp
            b = mub + mir*mub
        if b <=0: # balance paid off condition; exit loop
            break
        else: #reset balance; start with the next loop
            b = balance
            mfmp = mfmp + 10 
    print(mfmp)
    
def problem3(balance,air):
    mir = air/12
    # lower bound would be the minimum needed to be paid if there was no interest; therefore for monthly:(1/12 of starting balance)
    # upper bound would be the maximum we would pay in total with interest; therefore for montly:(1/12 of the total(balance+interest yearly))
    lower_bound = balance/12
    upper_bound = (balance*((1+mir)**12))/12
    epsilon = 0.01
    test_balance = balance
    while  abs(test_balance)> epsilon: # ends when win condition is hit
        mfmp = (lower_bound + upper_bound)/2 # minimum fixed montly payment calculated at the top of every iteration
        for i in range(12): # loop to create final balance based on current mfmp
            mub = test_balance - mfmp
            test_balance = mub*(1+mir)
        #test for whether the balance is paid off:
        if test_balance < -epsilon:  # mfmp too low condition: # detected when expression is above expected ; reassign lowerbound & test_balance 
            upper_bound = mfmp
            test_balance  = balance
        elif test_balance > epsilon: # mfmp too high condition: # detected when expression is below expected; reassign upperbound & test_balance for next iteration
            lower_bound = mfmp
            test_balance = balance
        
    # print out result
    print('-'*10)
    print("Lowest Payment:",round(mfmp,2))

if __name__ == "__main__":
    #problem1(42,0.2,0.04)
    #problem1(484,0.2,0.04)
    #problem2(3329,0.2)
    #problem2(4773,0.2)
    #problem2(3926,0.2)
    problem3(320000,0.2)
    problem3(999999,0.18)

