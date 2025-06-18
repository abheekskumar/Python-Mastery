# multiplication recursion
# a*b = a+a+a+a+a+... b times
# = a + a*(b-1)
# = a + (a + a*(b-2)).. and so on
# the base case(recursion end case) is when its a*1( the last multiplicative case) 
def mult_recursion(a,b):
    print(f"In {__name__},  function is running. ")
    if b == 1:#base case # end condition
        return a
    else:
        # recursive implementation
        return a + mult_recursion(a,b-1)

# factorial recursive implementation
# n! = n*(n-1)*(n-2).....*1
# = n*(n-1)!
# base case when number itself is == 1, return itself
def fac_rec(n):
    if n == 1:
        return 1
    else:
        return n*fac_rec(n-1)

if __name__ == "__main__":
    pass
    #print(mult_recursion(2,5))
    print(fac_rec(8))