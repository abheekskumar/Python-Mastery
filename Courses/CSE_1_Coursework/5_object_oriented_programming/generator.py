"""
any procedure with yield is a generator

yield stops the program execution and returns that value
the next time that program is run, it moves until the next yield 
until the last yield, this keeps happening, after which a StopIteration Exception is thrown.


They can be used to uniquely stop program execution.

It allows us to generate new objects as needed.
accessed with:
.__next__() method
"""

def genTest():
    yield 1
    yield 2

x = genTest()
print(x.__next__()) #1
print(x.__next__())# 2
#print(x.__next__())# StopIteration Error





# fib with a generator:
"""
The loop runs forever, it's just that execution is stopped every instance and we return that.
"""
def Fib():
    fibn_1 = 1 # fib(n-1)
    fibn_2 = 0 # fib(n-2)
    while True: # inf loop
        next = fibn_1 + fibn_2 # fib(n) = fib(n-1) + fib(n-2)
        yield next # return the next
        fibn_2 = fibn_1
        fibn_1 = next

inffib = Fib()
print(type(inffib))
print(inffib.__next__())
print(inffib.__next__())
print(inffib.__next__())
print(inffib.__next__())
print(inffib.__next__())


