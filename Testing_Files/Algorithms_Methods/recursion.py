"""
Recursion refers to calling a function within itself. The function is known as a recursive function.

You need to have 2 solutions:

The base case -- this is the final cases will be hit and then will return the appropriate format
The recursive case -- This is where the recursion will be called in the appropriate format

The challenge of implementing recursion is:
1) to write code that combines both of these solutions
2) return the appropriate type in the base case
3) call the recursion appropriately

Other remarks:
Compared to an iterative solution:
    Recursion is more likely than not more efficient(code-wise) from the programmer's perspective.
    However, more often than not, the space-complexity/constraint(memory usage) is greater than the 
        iterative case.
    Time complexity maybe the same

    Think of recursion as blocks that build below them, hit the base case and perish one by one returning the
        appropriate value in each perish.

"""

# recursive fib:
def recur_fib(n):
    # the fib sequence is defined as a given number being
        # the sum of the 2 previous numbers in a sequence.
    # base case: when n == 1 or n==0; then return 1
    # recursive case: when n is not either of those, return fib(n-1) + fib(n-2)
    if ((n == 0) or (n == 1)): # base case
        return 1 # flow of controls stops here if base cases are hit
    
    return recur_fib(n-1) + recur_fib(n-2) # recursive case

# recursive gcd: 
def recur_gcd(n1,n2):
    """
    Function used to return greatest common divisor. Implemented through Highest Common Factor(HCF) method
    Finding hcf is implemented by doing long division on 1 number by the other until you get itself.
    Therefore the base case is the number finding itself
    And the recursive case is redoing hcf until the base case is hit
    """
    if n2 == 0: # if the remaineder is finally 0, return n1, which would be what it's dividing by
        return n1
    return recur_gcd(n2,n1%n2) # recursive case, pass one number as is and define the other
                            # as the remainder of 1 number by the other(being the one that you just passed)
    

try:
    print(recur_gcd(6,9))
except Exception as e:
    print(e)
