def h(x):
    answer = 0
    s = str(x) 
    for c in s: # based on LENGTH of S, not size of x; here it simply grows
        # based on the size of the string, which does grow with n, but logarithmic
        # the size of the string is how many digits it has, which is based on the size of n,
        # but size grows much slower than the input in a logarithmic fashion. not with base 2 or 10, just some log
        answer += int(c)
    return answer


def fib_iter(n):
    a = 0 # first fib number
    b = 1 # second fib number
    ans = 0
    for _ in range(n-1): # this is linear time to compute
        
        # (n-1) cause a is the 0th in the sequence, b is the 1st number in the sequence. 
        # ans starts and the 2nd number, so for the nth number, it's (n-1)
        ans = a + b # sum of two prev seq numbers
        a = b # move up to current 1st previous number
        b = ans # next iteration, it would be up to par
    return ans

def recurmemo_fib(n,d={0:0,1:1}): # d holds the base cases
    if n in d:
        return d[n] # memoization
    else: #recursive case
        ans = recur_fib(n-1,d) + recur_fib(n-2,d) # double recursive call, but log?, (nope, it's 
        # linear)half of the exponential tree gets cut in half, I think eventually, only one branch should
        # be there
        d[n] = ans # store
        return ans # return
    
def recur_fib(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return recur_fib(n-1) + recur_fib(n-2) # double recursive call exponential growth
    
def sum_list(L):
    total = 0
    for ele in L:
        total += ele
    return total
    # linear in size of the list

# Complexity of common python functions:

"""
List:n is len(L):
O(1) - index, store, length, append, 
O(n) - ==, remove, copy, reverse, iteration, in list(membership)

Dictionary: n is len(d):
worst case:( we care about the worst case more)
O(n) - index, store, length, delete, iteration
average case:
O(1) - index , store, delete, iteration

"""