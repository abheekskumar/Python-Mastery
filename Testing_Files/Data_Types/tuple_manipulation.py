"""
Tuples are immutable; sequences
"""

"""
Few remarks:
functions can return tuples, and you can unpack them

tuples can be used to easily swap values of vars

x,y = y,x
"""

testTuple = tuple() # using constructor
testTuples = ()

tupOne = 2,3 # naturally, this is a tuple, you don't actually need to enclose them in brackets
tupTwo = 2, # this is type tuple because of the comma


t = "str1","str2","str3"
a,b,c = t
print(a,b,c)

"""
Tuples are more similar to strings.(Immutable)
the difference is being able to unpack, pack and more.
"""

# Tuple functions and methods

len(t)
max(t)
min(t)
t.count()
t.index()
