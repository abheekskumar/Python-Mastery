import sys

setOne = {} # this creates a type of dict
print(type(setOne)) # this is actually a dictionary
print(sys.getsizeof(setOne))


setOne = {3,2} # now it becomes a set
print(setOne)
print(type(setOne))
print(sys.getsizeof(setOne))



set