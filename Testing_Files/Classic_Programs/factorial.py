import traceback

def factorial_recur(num1):
    # function n! = n*(n-1)!
    # base case: when num1 == 1 or 0; return 1
    if num1 == 1 or num1 == 0:
        return 1
    elif num1>1:
    #recursive case: when num1 != (1 or 0); return n*factorial_recur(num1-1)
        return num1*factorial_recur(num1-1)
    else:
        return None
    
if __name__ == "__main__":
    try:
        print(factorial_recur(int(input("Enter a number for its factorial:"))))
    except Exception as e:
        pass
        print("The ",e,"has been thrown!")
        #print(traceback.format_exc())