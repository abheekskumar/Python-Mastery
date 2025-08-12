def iterPower_for(base,exp):
    ans = 1
    for i in range(1,exp+1):
        ans *= base
    print(ans)

def iterPower_while(base,exp):
    ans = 1
    i = exp # iteration variable
    while i > 0:
        ans *= base
        i -=1
    print(ans)

def iterPower_recur(base,exp):
    # ans(function) = base^exp
    # = base*base^(exp-1) # eq
    # = base * ans(function) of (base,exp-1)
    # base case: exp ==1; return 1; no it's not return 1, it's return base in the last case, one would be returning base itself, not 1
    if exp ==1:
        return base
    else:
        return base*iterPower_recur(base,exp-1) # recursion with a smaller value called
if __name__ == "__main__":
    pass
    iterPower_for(2,6)
    iterPower_while(2,6)
    print(iterPower_recur(2,6))