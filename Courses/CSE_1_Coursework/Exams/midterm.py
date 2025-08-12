"""
Problem 3:
Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences of the digit 7 in N.

For example:
count7(717) -> 2
count7(1237123) -> 1
count7(8989) -> 0
Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).

This function has to be recursive; you may not use loops! This function takes in one integer and returns one integer.
# Recursive solution:
remove the right most number using %10, check that, add if 7, continue with the rest of the digits
base case- len of digit = 1

"""
def count7(N):
    '''
    N: a non-negative integer
    '''
    # Base case, N< 10, it has to be == 7, otherwise don't add
    if (N < 10):
        if N == 7:
            return 1
        else:
            return 0

    if (N > 10):
        if N%10 == 7:
            return 1 + count7(N//10) # positive recursive case
        else:
            return count7(N//10) # negative rescursive case
        

#print(count7(1237123))


"""
Problem 4
Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.

assume L is not empty
assume 0 < n <= len(L)
This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.

Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list [[1, 1], [1, 1], [1, 1], [1, 4]]
"""
def getSublists(L,n):
    results = []
    temp = []
    l_count = 0
    while (l_count+n <=len(L)): # loop to keep track of where we're looking in the total list that stops when length of 
        # list is hit
        for i in range(n): # loop that calculates the sublists and adds them to temp
            temp.append(L[i+l_count])
        results.append(temp) # temp gets added to results and then reset
        temp = []
        l_count +=1 # counter to keep us checking the total sequence in check
    return results
#L,n= [10, 4, 6, 8, 3, 4, 5, 7, 7, 2],4

def getSublists(L, n):
    sublists = []
    a = len(L) - n + 1 # used to calculate the outer dimension directly
    for i in range(a):
        sublists.append(L[i:i+n]) # appropriately adds the correct slicing
    return sublists

#L, n= [1, 1, 1, 1, 4], 2
#print(getSublists(L,n))


"""
Problem 5:
Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)

This function takes in a dictionary and an integer and returns a list.
"""
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    
    results = []
    keys = aDict.keys()
    for key in keys:
        if aDict[key] == target:
            results.append(key)
    results.sort()
    return results
#print(keysWithValue({0: 2, 1: 1, 2: 0, 3: 0, 8: 0}, 1))


"""
Problem 6:
Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).

This function has to be recursive; you may not use loops!

This function takes in one integer and returns one integer.

recursive solution:
constantly return (right most digit) + func(rest of the digits)
base case, you're down to just 1 digit, then just return that one digit
"""
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N <10: # (N==0 can be used)we don't need this cause the modulus would just actually return that value, the
        #// remove unnecessary values
        return N
    else:
        return N%10 + sumDigits(N//10)
    
#print(sumDigits(126))


"""
Problem 7:

"""
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    L_idx = list()
    for idx in range(len(L)):
        if g(f(L[idx])) is True:
            pass
        else:
            L_idx.append(idx)
    L_idx.sort()
    L_idx.reverse()
    for i in L_idx:
        L.pop(i)


    if len(L) !=0:
        return max(L)
    else:
        return -1

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    filteredelements = []
    for i in L:
        if g(f(i)):
            filteredelements.append(i)
    L[:] = filteredelements # filters out all unwanted elements
    if L:
        return max(L)
    else:
        return -1
    
def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)