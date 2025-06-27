# zip function and zip object
"""
zip returns an iterator, not a list
an iterator can only be "consumed" once
"""
l1 = list("Hello world. This is Abheek.")
l2 = list("*"*len(l1))
x = zip(l1,l2)
print(type(x))
print(dict(x))
print(tuple(x))

# range 
"""
range also returns an iterator, but since it's lazy, it generates them on demand
hence you can use 

It's technically not an iterator; it's an iterator with constant time(__getitem__) but it behaves similarly to save
memory
"""

r = range(0,100)
print(type(r))
print(list(r))
print(tuple(r))


# map
"""
map is also lazy
"""
m = map(abs,[2,-23,24,26,-234])
m2 = map(str.upper,['balls',])
next(m2)
print(list(m2))
print(type(m))
print(list(m))
print(tuple(m)) # not printed
print(tuple(m2)) # also not printed, the iterables are already consumed


# filter
def multOfTen(n)-> bool:
    """
    Returns a boolean based on whether n is divisible by 10.
    """
    return (n%10 == 0)


f = filter(multOfTen,list(range(0,101)))
print(f)
print(type(f))
print(list(f))
print(tuple(f)) # not printed due to same reason

# shallow copy vs deep copy:
import copy 
l1 = list("Hello World.")
# shallow copy:
"""
Creates a new object, but doesn't copy over internal object pointers; they are shared
"""
l2 = copy.copy(l1)

# deep copy:
"""
Creates a new object, copies over the internal structure objects over perfectly
"""
l3 = copy.deepcopy(l2)

# functools
from functools import reduce
"""
Reduce: applies a function of 2 arguments cumulatively to the items of a sequence, reducing the sequence
to a single value.

reduce syntax: reduce(function,iterable) applies 
"""

numbers = list(range(1,6))
product = reduce(lambda x,y:x*y,numbers)
print(product)

# json
import json
L1 = list(range(1,100))
L2 = list(range(101,200))
dict1 = dict(zip(L1,L2))
s = json.dumps(dict1,indent= 2) # serialization into json formatted string
#print(s)
x = json.loads(s) # deserailiztion
fh = open("test_file.txt","w+")
json.dump(dict1,fh,indent = 2)
print(fh.readlines())
print('*'*200)
fh.close()