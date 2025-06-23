"""
Functions are reffered to as "first class objects":
    They have types
    can be elements of data structures like lists
    can appear in expressions
    
"""

def applyToEach(L,f):
    """
    assumes L is a list, f is a function
    mutates L by replacing each element, e, of L by f(e)
    """
    for e in range(len(L)):
        L[e] = f(L[e])

    applyToEach(L,abs) 
    applyToEach(L,int)
# Doing something to each element of a list using a function.


def  applyFuncs(L,x):
    """
    L is a list of functions, x is an arg.
    """
    for funcs in L:
        print(funcs(x))


"""
This is called higher order programming. Python has a generalization for this programming known as
map.

simple form- a unary function and a collection of suitable arguments
"""
x = map(abs,[1,-2,3,-4]) # produces an "iterable" that you can walk down
print(x)
print(list(x))
for i in x:
    print(i)

"""
General Form of Map- an n-ary function and n collections of arguments
"""
L1 = [1,28,36]
L2 = [2,57,9]
for elt in map(min,L1,L2): # min expects 2 arguments, now we have 2 lists...
    print(elt)