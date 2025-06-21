"""
Bisection search:
It is used to find a known value within a data structure that's sorted.

Time complexity:
log(n)

Usage:
It can be used for SORTED LINEAR STRUCTURES

General Idea: 
It works by comparing the average value of the first and the last 
element(which would be the middle value) to the value we want. 

Based on this comparison, we reduce the search spare every time. 
The search space is reduced by half. Hence it has log(n) time complexity.

General Implementation:
We use an iterative loop to continusouly reduce the search space to get what we want.
We have to be careful about the way we stop that search. 
Think about cases where the element doesn't actually exist.

Other Remarks:
We often use an epsilon value and then compare(eg: abs(a-b) <= epsilon)) where epsilon is a small positive number.
Search space depends on the question you have and what you're actually trying to optimize for.

"""

def bisection_square(n):
    # Search Space: we're guessing from 1 to number n
    # condition: (guess**2) should be close to n
    # implementation: through using epsilon
    # In these cases, there isn't a situation where what we want doesn't exist. We can look 
    # at formatting the number if you want
    epsilon = 0.1
    low = 0
    high = n
    guess = (low+high)/2
    numGuesses = 0
    while (abs(guess**2-n) > epsilon): # inverted of end condition
        # Debug print Statements:
        print(guess)
        numGuesses +=1 # Guess is always being made when we enter the loop. Therefore, we can count at the top.
        guess = (low+high)/2
        if guess**2 > n: # guess is too high, therefore it actually exists below; change high to current guess
            high = guess
        else: # only other case in this loop, therefore number is too low, raise the low bar to current guess
            low = guess
    return(guess,numGuesses) # returns the guess it founc


def bisection_cube(n):
    # Search Space: from 0 to number n
    # condition: if abs(n-guess) <= epsilon(small positive number)
    # this would run into an inf loop for n < 1(search space is invalid for that loop)
    epsilon = 0.1
    low = 0
    high = n
    guess = (low+high)/2
    numGuesses = 0
    while (abs(guess**3-n) > epsilon): # inverted win condition
        numGuesses +=1
        if guess**3 > n: # guess is too high, reset high to current guess
            high = guess
        else: # guess is too low, reset low to current guess
            low = guess
        guess = (low+high)/2 # recalculate guess based on above constraints before the next iteration starts
    
    return guess, numGuesses # returns tuple of guess and num of guesses it took to get there.


def bisection_square_frac(n):
    # this is a different case; the search space is different from the above 2 questions as we're 
    # dealing with fractions
    # here search case would be from given number(n) up till 1 as fractions reduce when squared. 
    # naturally we stop at 1 because after that, the square of the number wouldn't be a fraction
    # this would run into an inf loop if n > 1( search space is invalid for that input)
    low  = n
    high = 1
    middle = (low+high)/2 # middle is the same as guess var from above
    epsilon = 0.0001  # we need a smaller epsilon value this time
    numGuesses =0
    while (abs(middle**2 - n) > epsilon): # invertion of end condition
        if middle**2 > n : # guessed too high; reset high
            high = middle
        else: # guessed too low; reset low
            low = middle
        numGuesses +=1 # calculate number of guesses
        middle = (low+high)/2 # recalculate guess

    return middle, numGuesses

    # you can implement bisection_cube_frac

if __name__ == "__main__":
    pass
    #print(bisection_square(25))
    #print(bisection_cube(27))
    print(bisection_square_frac(9/3))