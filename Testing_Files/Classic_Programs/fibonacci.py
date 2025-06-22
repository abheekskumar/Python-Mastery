count = 0
def recur_fibonacci(num1):
    # counter to reduce term output by 1.
    global count
    if count == 0:
        num1 -=1
    count +=1


    # base case: num1 == 1 or 0; return 1
    if num1 == 1 or num1 == 0:
        return 1
    return recur_fibonacci(num1-1) + recur_fibonacci(num1-2)

def iter_fibonacci(n):
    # fib of a term is the addition of the previous two terms in the sequence
    if n == 0:
        return 1
    a = 0 # first no. of fib seq
    b = 1 # second no. of fib seq
    # [a,b,ans] structure
    for _ in range(1,n+1): # loop for "n" number of terms. Offset to start from 1
        ans = a + b # adds the previous 2 terms
        a = b
        b = ans
    return ans # return the final ans

if __name__ == "__main__":
    print(recur_fibonacci(int(input("Enter a number for the fibonacci:"))))
    print(iter_fibonacci(int(input("Enter the term to find the fibonacci number of that term:"))))