"""
Using memoization, write fibonacci recursive code, with the dictionary being empty: handle
base cases in the function itself.
"""
fibCount = 0
def fib(n,d={}) -> int:
    """Recursive fib with memo."""

    # global counter implementation
    global fibCount 
    fibCount +=1


    if n in d: # checking if number in memo/hash
        return d[n]
    if n == 1: # base case for number ==1
        return 1
    if n == 0: # base case for number ==2
        return 1
    ans = fib(n-1,d) + fib(n-2,d)
    d[n] = ans
    return ans

print(fib(float(input("Enter a number for it's fib:"))))
print(f"Hash fib ran {fibCount} times.")