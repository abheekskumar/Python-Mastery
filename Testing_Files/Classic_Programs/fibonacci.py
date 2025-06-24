numRecur=0
numIter = 0
numMemo= 0
def recur_fibonacci(num1):
    # counter 
    global numRecur
    numRecur +=1
    # base case: num1 == 1 or 0; return 1
    if num1 == 1 or num1 == 0:
        return 1
    return recur_fibonacci(num1-1) + recur_fibonacci(num1-2)

def iter_fibonacci(n):
    # fib of a term is the addition of the previous two terms in the sequence
    global numIter
    if n == 0:
        return 1
    a = 0 # first no. of fib seq
    b = 1 # second no. of fib seq
    # [a,b,ans] structure
    for _ in range(1,n+1): # loop for "n" number of terms. Offset to start from 1
        numIter +=1
        ans = a + b # adds the previous 2 terms
        a = b
        b = ans
    return ans # return the final ans

def memo_fib(n,d={1:1,0:1}): # default d has base conditions
    """
    Fibonacci number using memoization with dictionaries
    """
    global numMemo
    numMemo +=1

    if n in d:
        return d[n] 
    else:
        ans = memo_fib(n-1,d) + memo_fib(n-2,d) # d has to be called only then will the values be rememberd
        # otherwise, the default values will take over
        d[n] = ans
        return ans



if __name__ == "__main__":
    n = int(input("Enter a number for the fibonacci:"))
    print(recur_fibonacci(n))
    print(f"Number of times Recursive Fib was called is {numRecur}")
    print(iter_fibonacci(n))
    print(f"Number of times iterative fibonacci loop ran is {numIter}")
    print(memo_fib(n,d))
    print(f"Number of times memoization fibonacci recursive calls = {numMemo}")