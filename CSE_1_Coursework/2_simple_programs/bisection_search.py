def bisection_squareroot():
    sqr = int(input("Enter an integer:"))
    low = 0
    high = sqr
    guess = (low + high)/2
    epsilon = 0.1

    while abs((guess**2)-sqr) > epsilon: # negation of true condition # end sceanario
        guess = (low + high)/2 # redifine every loop run
        if guess**2 > sqr:# guess is too high; reduce bisection
            high = guess # last definition before jumping to a new iteration
        elif guess**2 < sqr: # guess is too low; increase bisection
            low = guess # last definition before jumping to a new iteration

    print(low)
    print(guess)
    print(high)

def bisection_cube_root():
    cube = eval(input("Enter a number:"))
    if 1 > abs(cube) > 0: # changing the search space based on the type of number
        #fraction case
        low = cube
        high = 1
        epsilon = 0.00000000000000000001
    else:
        low = 0
        high = cube
        epsilon = 0.01
    num_guesses = 0
    guess = (low+high)/2

    while (abs((guess**3)-cube) > epsilon) and (guess <=cube): # winning/stopping condition and (prevents inf loop)
        if guess**3 > cube: # guess is too high; lower upperbound
            high = guess
        else: # guess is too low; increase lowerbound
            low = guess
        # redefine new guess
        guess = (low+high)/2
        num_guesses +=1



    # check for actual/ close:

    print(num_guesses)
    print(low)
    print(guess)
    print(high)
import traceback
def guess_my_num():
    try:
        num = int(input("Enter a number between 1(inclusive) and 100(exclusive)."))
        if 100> num >= 1:
            # bisection search
            high = 100
            low = 0
            guess = (high+low)/2
            while (guess!=num):
                if guess > num: # guess is too high, reduce upperbound
                    high = guess
                elif guess < num: # guess is too low, increase lowerbound
                    low = guess
                else: # guess == num
                    break
                guess = (low+high)/2 # change to new guess based on search space
                print(guess)
            
        else:
            print("Improper input.")
    except Exception as e:
        print("exception thrown.")
        print(e)
        print(traceback.format_exc())
import math
def guess_my_num_v2():
    # guess based on 
    print("Let's play a game where I guess your number.")
    low = 0
    high = 100
    guess = (low+high)/2
    while True:
        guess = (low + high)/2
        guess = round(guess)
        print(f"Is your guess {guess}")
        inp = input("Enter 'h' to indicate higher. Enter 'l' to indicate lower. Enter 'c' to indicate correct guess:")
        if inp == 'h':
            low = guess
        elif inp == 'c':
            print(f"Game over, your number was {guess}")
            break # game over condition
        elif inp == 'l': 
            high = guess





if __name__ == "__main__":
    pass
    #bisection_squareroot()
    #bisection_cube_root()
    #guess_my_num()
    guess_my_num_v2()