# used for root finding of polynomial of any degree, but 1 variable
# it states that if g is a good guess, (g-((p(g))/(p'(g)))) is a better guess; where p is said polynomial and p' is the derivative.

# square root through newton raphson method:
def nr_square_root(num):
    # the polynomial would be: p(x) = x^2 - num
    # the derivative of the polynomial would be:p'(x) = 2x
    guess = num/2
    epsilon = 0.01
    num_guesses =0
    while abs(guess**2-num) > epsilon: # end condition reversed
        guess = guess - (((guess**2-num))/(2*guess))
        num_guesses +=1  
    print(num_guesses)
    print(guess)

def nr_cube_root(num):
    # the polynomial is : p(x) = x^3 -num
    # the derivative of said polynomial would be : p'(x) = 3x^2
    pass
    guess = num/2
    epsilon = 0.01
    num_guesses = 0
    while abs(guess**3-num) > epsilon:
        num_guesses +=1
        guess = guess - ((guess**3 - num)/(3*(guess**2)))
    print(num_guesses)
    print(guess)



numGuesses = 0
def nr_fourth_root(num: int) -> int:
    """Finds the fourth root of num. """
    global numGuesses
    numGuesses +=1
    # f(x) = x^4 - num
    # f'(x) = 4x^3
    # NR: if g is a guess, g - p(g)/p'(g) is a better guess where p(x) is polynomial of any degree, but one variable.
    # here p(g) = guess**4 - num
    # p'(g) = 4*(guess**3)
    guess = num/2
    epsilon = 0.1
    while (abs(guess**4-num) > epsilon):
        guess -= ((guess**4 - num)/(4*(guess**3)))
    print(guess,numGuesses)

if __name__ == "__main__":
    #nr_square_root(24)
    #nr_square_root(54)
    # nr_cube_root(27)
    # nr_cube_root(8)
    nr_fourth_root(256)
    
