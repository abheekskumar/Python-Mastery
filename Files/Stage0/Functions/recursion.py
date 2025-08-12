"""
Recursion refers to calling a function within itself. The function is known as a recursive function.

You need to have 2 solutions:

The base case -- this is the final cases will be hit and then will return the appropriate format
The recursive case -- This is where the recursion will be called in the appropriate format

The challenge of implementing recursion is:
1) to write code that combines both of these solutions
2) return the appropriate type in the base case
3) call the recursion appropriately

Other remarks:
Compared to an iterative solution:
    Recursion is more likely than not more efficient(code-wise) from the programmer's perspective.
    However, more often than not, the space-complexity/constraint(memory usage) is greater than the 
        iterative case.
    Time complexity maybe the same

    Think of recursion as blocks that build below them, hit the base case and perish one by one returning the
        appropriate value in each perish.
Direct vs Indirect Recursion:
    Direct is as expected
    Indirect is when another function calls a different function recursively
"""

# recursive fib:
def recur_fib(n):
    # the fib sequence is defined as a given number being
        # the sum of the 2 previous numbers in a sequence.
    # base case: when n == 1 or n==0; then return 1
    # recursive case: when n is not either of those, return fib(n-1) + fib(n-2)
    if ((n == 0) or (n == 1)): # base case
        return 1 # flow of controls stops here if base cases are hit
    
    return recur_fib(n-1) + recur_fib(n-2) # recursive case

# recursive gcd: 
def recur_gcd(n1,n2):
    """
    Function used to return greatest common divisor. Implemented through Highest Common Factor(HCF) method
    Finding hcf is implemented by doing long division on 1 number by the other until you get itself.
    Therefore the base case is the number finding itself
    And the recursive case is redoing hcf until the base case is hit
    """
    if n2 == 0: # if the remaineder is finally 0, return n1, which would be what it's dividing by
        return n1
    return recur_gcd(n2,n1%n2) # recursive case, pass one number as is and define the other
                            # as the remainder of 1 number by the other(being the one that you just passed)
    

# recursive palindrome:
def recur_palindrome(s1):
    # base case: len of string is 1 or 0, it's already a palindrome
    # Recursive case: check outer most characters(first & last), if they're equal,
    # recursively check everything in between

    if len(s1) == 1:
        return True
    if (s1[0]==s1[-1]): # condition that checks for palindrome
        return recur_palindrome(s1[1:-1]) # due to string slicing exclusion, it means everything in between
    else: 
        return False # if any of the characters fail, return False

# recursive sum of natural numbers
def recur_sum_natural(n):
    # the problem can be defined as: sum(n) = n + sum(n-1)
    #base case: when n == 1: return 1
    # recursive case: else return n + recur_sum(n-1)

    if n == 1:
        return 1
    else: 
        return n + recur_sum_natural(n-1)
# recursive sum of AP:
# t(n) = a + (n-1)*d # nth term of an ap
# s(n) = n*(a + a(n-1)*d)/2  # sum of n terms of an ap
# in terms of recursion, s(n) = nth term + s(n-1)
# base case wouljd be when n == 1, return just 'a'

def recur_sum_ap(n,a,d):
    if n == 1:
        return a
    else:
        return (a + (n-1)*d) + recur_sum_ap(n-1,a,d)

# recursive summation of GP
# recursively thinking about the problem, we have:
# s(n) =  nth term + s(n-1) # this is for all summations,
# the only logic that changes is the 'nth' term of whatever...
# the nth term of a GP is = a*r^(n-1)
# sum of gp = a(1^n-r^n)/(1-r)

def recur_sum_gp(n,a,r):
    if n == 1:
        return a
    else:
        return ((a*(r**(n-1))) + recur_sum_gp(n-1,a,r))
    
# Multiplicaiton as recursive addition:
# add add n1 to itself n2 times
# base case is when n2 == 1, return just n1
# recursive case: else return n1 + mult_recur(n1,n2-1)
def recur_add_mult(n1,n2):
    if n2 == 1:
        return n1
    else:
        return n1 + recur_add_mult(n1,n2-1)
    

# recursive & bisection isIn: check if char is in a string or not
def isIn(char,aStr):
    """
    char - a single character
    aStr - a string 
    Returns index position of char in aStr if present, else returns False
    """
    # low is removed as it's not needed as string indexing always starts from 0
    high = len(aStr)
    middle = int((high)/2)
    #middle = high//2 # conservative estimate
    x = aStr[middle]

    # bases case for smaller search spaces:
    if len(aStr) == 1:
        return (char == aStr)  # Depends on whatever this character is
    elif len(aStr) == 0:
        return False # negative base case
    # this has to be run until it's found or
    
    if char == x:
        return True # Traditional Base case
    else: # recursive cases
        if char > x: # 
            return isIn(char,aStr[middle+1:]) # the +1 excludes the current 'x' character from search space
        else: # case when  char < x
            return isIn(char,aStr[:middle]) # the middle will be excluded due to python slicing rules


    
def isInStarter(char,aStr):
    """
    Cleans the string and character and then calls the recursive func
    """
    char = char.lower()
    aStrCleaned = ""
    for i in aStr:
        if i in "abcdefghijklmnopqrstuvwxyz":
            aStrCleaned += i
    aStr = aStrCleaned

    #Checking other criteria
    if len(char) !=1:
        return None
    print(char,aStr)
    # call main func now:
    return isIn(char,aStr)

try:
    pass
    #print(recur_gcd(6,9))
    #print(recur_palindrome("racecar"))
    #print(recur_sum_natural(23))
    #print(recur_sum_gp(5,1,2))
    #print(recur_add_mult(2,3))
    t1 = 'f', 'bdefhllmsuvvvxyyyyz'
    t2 = "a", "bbcdkkknortuuvw"
    print(isInStarter(t1[0],t1[1]))
    print(isInStarter(t2[0],t2[1]))
except Exception as e:
    print(e)
