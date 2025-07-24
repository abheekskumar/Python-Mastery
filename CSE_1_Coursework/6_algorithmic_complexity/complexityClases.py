 # constant complexity:
def constLookup(L):
    return L[0] # always returns the first element

# logarithmic complexity
# bisection search, binary search of a list
def intToStr(i):
    digits = "0123456789"
    if i ==0:
        return "0"
    res = ""
    # until here, constant

    while i > 0: # loop gets reduced by a factor of 1/10 each time, hence we go through this
        # log10(i) times.
        res = digits[i%10] + res # inside loop constant
        i = i//10
    return res # constant

# linear complexity:
# searching a list, adding a string containing digits
def addDigits(s):
    val = 0 # constant
    for c in s: # goes through this for size(s)
        val += int(c) # constant
    return val # constant

def fact_iter(n):
    prod = 1
    for i in range(1,n+1): # depends on how many times do you go around the loop?
        prod *= i
    return prod


def fact_recur(n):
    if n == 1 or n == 0: # base case
        return 1
    return n*fact_recur(n-1) # recursive case

# even in this case, it's linear because the recursive is called n times. 
# recursive might be a bit slower, but same order.( inthe asymtotic case, it's the same)
# iterative call might be a bit more space efficient.


#Polynomical complexity
# commonly occurs when we have nested loops or recursive costs(where there are some additional costs related 
# to input?)

def isSubset(L1,L2):
    for ele1 in L1: # takes 1 element
        matched = False
        for ele2 in L2: # compares that 1 element to all the other elements in the second list
            if ele1 == ele2:
                matched = True
                break
        if not matched: # if not found for all elements inthe 2nd list, return false
            return False
    return True # once every L1 element is in L2, return True
"""
O(len(l1))*O(len(l2)) = O(len(l1)*len(l2))
assuming len(l1) == len(l2) assigned n
O(n^2)
"""

def intersect(L1,L2):
    tmp = []
    for ele1 in L1: # through all elements of L1
        for ele2 in L2: # through all elements of L2
            if ele1 == ele2:
                tmp.append(ele1)
    
    res = []
    for ele in tmp: # through all the elements in tmp
        if ele not in res: # shouldn't this also be O(len(res))? and hence maybe be a bit less than n^2 
            res.append(ele)
    return res
"""
O(len(l1)*len(l2)) + O(len(tmp)*O(len(res)))
assume len(l1) == len(l2); hence len(L1) should also be len(tmp) and res should grow to the same size, but 
a bit behind right? how would You express that quantitatively?
"""

def g(n):
    x = 0
    for _ in range(n):
        for _ in range(n):
            x +=1
    return x

"""
classic n^2 problem
"""

# Exponential Complexity
# often a recursive function that calls itself, but multiple calls
# should also be fib
# generally, in exponential problems, we aim for an approximate solution.

def genSubsets(L)-> list:
    """ Returns a list of all the subsets of \"L\""""
    if len(L) == 0: # base case
        return [[]] # a list containing an empty list
    """ this solution is similar to that of the towers of hanoi.
    We generate subsets for all but the last element
    """
    smaller = genSubsets(L[:-1]) # 
    """ We take that last element"""
    extra = L[-1:] # list of just the last element
    new = []
    for small in smaller: # all subsets without the last element
        new.append(small+extra) # for each subset without the last element, add the last element

    return smaller+new # return the combined solution that holds all but the last elements and all 
# with the last element

# time complexity analysis:
def genSubsets(L) -> list:
    """ Returns a list of all the subsets."""
    # base cases
    if len(L) == 0:
        return [[]] 
    # recursive cases
    smaller = genSubsets(L[:-1]) # this costs time
    """for a size of "k" elements, we have 2^k possibilities. for each element, we decide ig it's in or not(2 options)
     this then extends to every element(2^(n-1) + 2^(n-2)... to 2(0)) till the base case.
    """

    last = L[-1:]
    new = []
    for small in smaller: # this costs time
        """ """
        new.append(small+last)

    return smaller + new

    

    