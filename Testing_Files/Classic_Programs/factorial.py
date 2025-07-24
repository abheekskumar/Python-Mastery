import traceback
import json
import sys
memo ={"0":1,"1":1} 
sys.setrecursionlimit(100000)
# print(sys.getrecursionlimit())



def factorial_recur(num1,memo):
    # function n! = n*(n-1)!
    # base case: when num1 == 1 or 0; return 1
    if str(num1) in memo:
        return memo[str(num1)]
    
    #recursive case: when num1 != (1 or 0); return n*factorial_recur(num1-1)
    else:
        # no. of computations
        global numComputation
        numComputation +=1

        ans = num1*factorial_recur(num1-1,memo)
        memo[str(num1)] = ans
        return ans
    
    
def factorial_iter(num2):
    # factorial : n! = n*(n-1)*(n-2)...*1
    if num2 == 0:
        return 1
    ans = 1 # var to keep track of ans
    for i in range(1,num2+1): # list generated to make valid i values; for loop goes through each iteration
        # to execute "updating ans var" constantly
        ans = i*ans # updating ans var with i*new_ans
    return ans


if __name__ == "__main__":
    try:
        #reading memo
        with open("factorial_memo.json","r") as fh:
            memo = json.loads(fh.read())

        while input("Continue?:"): # loop for controlling when we can exit
            numComputation = 0
            print(factorial_recur(int(input("Enter a number for its factorial:")),memo))
            print(f"The number of computations for that calculations was:{numComputation}")

        # writing memo
        with open("factorial_memo.json","w") as fh:
            fh.write(json.dumps(memo,indent = 4))

    except Exception as e:
        print("Dunder name, main Block.")
        print("The ",e,"has been thrown!")
        print(traceback.format_exc())

        # writing memo
        with open("factorial_memo.json","w") as fh:
            fh.write(json.dumps(memo,indent = 4))