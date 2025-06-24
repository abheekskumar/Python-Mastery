
numRecurFib = 0
numMemoFib =0

def recur_fib(n):
    global numRecurFib # breaking a scope
    numRecurFib +=1 # keeping track of number of times called
    """
    Recursive fibonacci
    Proposed time complexity: 2^n due to 2 recursive calls
    """
    if n ==1 :# base case
        return 1
    elif n ==2 :
        return 2
    else: # recursive case
        return recur_fib(n-1) + recur_fib(n-2)
    # very ineffcient

"""
This is efficient method of implementing fib using dicts. This uses a process called
memoization. You remember all the values you've stored.
"""
def dict_fib(n,d):
    global numMemoFib
    numMemoFib +=1

    if n in d: # checks if a given value is in the dict
        return d[n] # if it is, return the requested value
    else: # if a given value isn't in the dict, compute it recursively:
        ans = dict_fib(n-1,d) + dict_fib(n-2,d) 
        d[n] = ans # add to dict once base case(added to dict) are hit 
        return ans # return and cascade it back
    
d = {1:1,2:2}
n = 2
print(dict_fib(n,d))
print("Number of times Dict/Memo version called:",numMemoFib)

print(recur_fib(n))
print("Number of Times Recur version Called:",numRecurFib)

