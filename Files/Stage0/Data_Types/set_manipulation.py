import sys

setOne = {} # this creates a type of dict
print(type(setOne)) # this is actually a dictionary
print(sys.getsizeof(setOne))


setOne = {3,2} # redefinition with only stand alone elements, not key:value pairs, 
 # hence a set
print(setOne)
print(type(setOne))
print(sys.getsizeof(setOne))

# to directly construct a set:
setTwo =set() # use the set constructor

# iteration through a set:
print("Iteration:")
for ele in setOne:
    print(ele)

# set mutability:
"""
sets are mutable
"""
print(id(setOne))
setOne.add(24)
print(id(setOne))



# set functions and methods:


setOne.add() # adds an element, sets are unique
setOne.clear() # removes all elements
setOne.copy() # creates a shallow copy in a memory location
setOne.difference() # returns a new set that doesn't have elements shared between the iterable
setOne.difference_update() # updates the set, removing elements found in the iterable
setOne.discard() # removes an element from a set; no error raised if not found
setOne.remove() # removes an element from a set; error raised if not found
setOne.intersection() # returns a new set with common elements with iterable
setOne.intersection_update() # updates the set with only common elements found with iterable
setOne.isdisjoint() # returns true if 2 sets have null intersection
setOne.issubset() # retunrs true if other set contains this set
setOne.issuperset() # returns true if this set contains other set
setOne.pop() # removes and returns an element
setOne.union() # returns a new set with all the same elements from the other set
setOne.update() # updates this set, adding elements from the other
setOne.symmetric_difference() # returns a new set of elements that are in either set, but not both
setOne.symmetric_difference_update() # updates set wiht elements in either set, but not both
