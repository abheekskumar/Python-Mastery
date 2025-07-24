def fib(n):
    # function : f(n) = f(n-1) + f(n-2)
    #base cases:
    if n == 1 or n == 0: # n <=1
        return 1
    else: # recursive case
        return fib(n-1) + fib(n-2)
    
if __name__ == "__main__":
    print(fib(6))