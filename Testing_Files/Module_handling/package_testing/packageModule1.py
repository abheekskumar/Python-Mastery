
test = 23
def memoFib(num:int,d = {0:0,1:1}) -> int:
    """Fibonacci implementation with memoization."""
    if num in d:
        return d[num]
    ans = memoFib(num-1,d) + memoFib(num-2,d)
    d[num] = ans
    return ans

