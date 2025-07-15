"""
Search algorithms:

method of finding an item or a group of items with a specific property within a collection of items.

collection could be implicit:
    exhaustive enumeration
    bisection search
    newton-raphson
collection could be explicit:
    a student record within a stored collecition of data.

Linear search:
    brute force search
    list does not have to be sorted

Bisection Search:
    list must be sorted
    2 implementation

"""

# linear search:
def linear_search(L,e):
    for i in range(len(L)):
        if e == L[i]:
            return True
    return False
"""
worst case:
O(len(L))*O(1) = O(len(L)) or O(n) where n = len(L)
O(1) comes from e== L[i], which assumes that one can retrieve an element from the list in constant time:
if L = list[int] : all the ints are next to each other in memory and say that each takes 4 bytes of space.
    we can just count from the start(base) to the ith element by doing: base + 4*i

if L = list(heterogeneous), it's an array(of contiguous addresses) that holds pointers/references to 
    the other object in memory.

in both these cases, we can access the elements in constant time, we just move to that index and then 

"""

# linear serach  on sorted:
def serach(L,e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        elif L[i] > e:
            return False
    return False
# a bit better for average case, but in the worst case, it's still linear O(n)


# bisection 1:
def bisectionSearch1(L,e):
    """ Assumes L is sorted"""
    if L == []:
        return False # negative base case
    elif len(L) == 1:
        return L[0] == e # if it's the only element, return that
    else:
        half = len(L)//2 # calculate the half index
        if e == L[half]:
            return True
        elif e < L[half]: # it's in the lower half
            return bisectionSearch1(L[:half],e) # making a copy of the list increases the complexity
        # it isn't log(n)
        else:
            return bisectionSearch1(L[half+1:],e)
"""
This stops when 1 = n/(2^i)
n = 2^i
i = log2(n), where n is the length of the list
O(log(n))

In this implementation of binary search, since we make a copy, it isn't just log(n) complexity
this is nLog(n)

"""
def bisectionSearch2(L,e):
    def bisectionSearch2Helper(L,e,low,high):
        if low == high: # in the case of 1 element left to check; return that check
            return L[low] == e
        
        half = (low+high)//2 # integer division takes a conservative case
        if L[half] == e: # positive base case
            return True
        
        elif L[half] > e: # if element exists in lower half
            if low == half: # no element is left to check, that conservative characteristic hits
                # the lower bound
                return False
            else:
                return bisectionSearch2Helper(L,e,low,half-1) # -1 to exclude that element
        else: # element is in the upper half
                return bisectionSearch2Helper(L,e,half+1,high) # -1 to exclude that element
            
    ######
    # using a helper cause you cannot call this recursively with this implementation otherwise
    # also to check len(L) == 0 base case
    if len(L) == 0:
        return False
    else:
        return bisectionSearch2Helper(L,e,0,len(L)-1)
"""
This implementation just uses the same list, but changes the search space.
2 pointer approach

this is O(log(n))

"""

l = [23,265,266,288,1024]
e = 23
print(bisectionSearch1(l,e))
print(bisectionSearch2(l,e))

"""
For an unsorted list, you can amortize the cost if you perform multiple searches.

if you only do seraching once:
SORT[O(n)] + O(log(n)) < O(n) # using linear[O(n)] is better
if you plan on searching many times, it is better to sort and then use bisection
for a large number of a searches(after sorting), it can pay off to sort the list first.
"""
        