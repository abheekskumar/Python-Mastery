"""
lambda functions are anonomous functions that have no return statement defined.
it's used for simple functions.
That's why they don't have names.
"""

x = lambda x: x%2==0 # creates a lambda procedure, but no name is binded to it.
b = lambda x,y: x%y == 0




print(x(2))
print(x(3))
print((lambda x: x==2)(2))

