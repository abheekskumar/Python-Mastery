"""
time and space efficiency.
How do we measure an algorithm's efficiencies?
    timer, count no. of operations, abstract notion of order of growth(most appropriate the efficiency)

    timer - changes on different computers, a lot of problems need to be tested
    coutning- which operation to count? depends on implementation(a bit better, computer indendent)
    we want to express the growth of a program based on the upper bound on the growth
    we look and decide at the largest factors
    growth of a programs time

    constant - doesn't depend on input
    linear - scales with input
    quadratic - scales but faster
    logarithmic - scales, but then slows down at each step
    linear* logarithmic - worse than linear, but better than quad
    exponenetial - scales terribly


    Measuring order of growth: Big Oh Notation:
    measures an upper bound on the aysymtotic growth, often called the order of growth
    Big Oh or O() is  used to describe the worst case
    - it can occur often and is usually the bottleneck when a program runs.
    - express rate of growth with respect to input size
    - independent of computer and depends on the algorithm

    -ignores additive constants
    -ignore multiplicative constants    

    Big Theta Notation :
    - the big theta bound is a lower and upper bound on the growth of some function
    - theta bounds are preferred because they are "tight", they talk about not only the worst case, but 
    also the best case FOR a particular input.
    - since this is more input dependent(for the lower bound) than the big Oh notation, we use theta(input, not 
    just expressed on terms of n)
    - but also use the same rules( law of dominance, law of multiplication, law of addition)

    Big Omega Notation:
    - best case for an algorithm. 
    - defines only the lower bound.

"""

def iter_fib(n):

    answer = 1 # 1 step
    # loop runs n-1 times
    # so total loop is 5(n-1) = 5n - 5
    while n > 1: # 1 step
        answer = answer*n #2 steps
        n = n-1 # 2 steps
    return answer # 1 step

# total I'm getting 5n - 3, actual answer is 5n-2

# focus on the dominant terms that grows in the worst case.


"""
Complexity classes ordered low to high:

O(1) - constant
O((log(n))) - logarithmic
O(n) - linear
O(n(log(n))) - loglinear
O(n^c) - polynomial 
O(c^n) - exponential
O(n!) - factorial

"""


"""
Law of addition for Big Oh Notation: for sequential statements

O(f(n)) + O(g(n)) = O(f(n)+g(n))
ex:
"""
n = 0
for x in range(n):
    pass
for y in range(n*n):
    pass
"""
O(n) + O(n^2) = O( n^2 + n) = O(n^2)

Law of multiplication: for nested loops

O(f(n))*O(g(n)) = O(f(n)*g(n))
"""
n = 0
for x in range(n):
    for y in range(n**2):
        pass
""" O(n)*O(n^2) = O(n^3)"""


