"""
Newton Raphson:
This is the most efficient guessing method that I know of right now.
This method is also based on guessing.

The method states that:

If G is a good guess,  g - ((p(g))/(p'(g))) is a better guess
p(x) is a function where the problem is defined
p'(x) is a derivative

This is valid for SINGLE variable functions with any degree. 
Therefore, the polynomial p(x) should be a single variable polynomial with any degree.
"""

def nr_square_root(n):
    # This is a square root function.
    # defined as p(x) = x^2 - n; where n is the number that they've given
    # then p'(x) = 2x

    # inital guess can just be n/2, it's the same first guess as bisection search.( high/2)

    guess = n/2
    epsilon = 0.1
    numGuesses = 0
    while (abs(guess**2-n)> epsilon):
        numGuesses +=1
        guess = guess - ((guess**2-n)/(2*guess)) # Newton Raphson Method implemented
    
    return guess, numGuesses

def nr_cube_root(n):
    # In this case, the p(x) = x^3 -n
    # Then, p'(x) = 3x^2 
    # once again, first guess can just be n/2

    guess = n/2
    epsilon = 0.1
    numGuesses = 0
    while (abs(guess**3-n)>epsilon): # inverted win condition
        numGuesses +=1
        guess = guess - ((guess**3-n)/(3*(guess**2)))

    return guess, numGuesses


if __name__ == "__main__":
    pass
    #a,b = nr_square_root(25)
    #print(a,b)
    print(nr_cube_root(27))



