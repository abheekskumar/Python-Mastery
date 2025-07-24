# guess and check or exhaustive enumeration:
# you go through all possible values and guess each one.
# time complexity of n(go through all possible sceanarios)
# In this implementation, you could blow right across the number you're trying to find out. 
# have measures in place for that too
def basic_cube(n):
    for guess in range(1,n+1):
        if guess**3 == n:
            print(guess)
            break

def approximate_cube(n):
    guess = 0
    epsilon = 0.0001
    increment = 0.1
    numGuesses =0
    while abs(guess**3-n) > epsilon:
        if guess**3 == n:
            print(guess)
            break
        guess +=increment
        numGuesses +=1
    print(guess,numGuesses)

if __name__ == "__main__":
    approximate_cube(27)