"""
Lambda Functions are used in cases for defining a very small or minimal functions
Think of them as objects.
You can pass vars through to them by sending them through parenthesis next
to the lambda fucntion object

eg:
(lambda fucntion object)(vars passed to it)

"""

y = (lambda x,y: x+y) # y is now a lambda function
print(y(2,3))
x = (lambda x,y: print(x+y)) # can directly define print statements
x(2,3)

