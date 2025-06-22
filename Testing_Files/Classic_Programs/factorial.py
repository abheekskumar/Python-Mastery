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
        print(factorial_recur(int(input("Enter a number for its factorial:"))))
        print(factorial_iter(int(input("Enter a number:"))))
    except Exception as e:
        pass
        print("The ",e,"has been thrown!")
        #print(traceback.format_exc())