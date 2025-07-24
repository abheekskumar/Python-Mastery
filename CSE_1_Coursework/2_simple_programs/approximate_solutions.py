def guess_cube():
    cube = float(input("Enter an integer:"))
    epsilon = 0.001
    increment = 0.1
    guess = 0
    while abs((guess**3)-cube) >= epsilon:
        guess +=increment

    
    if cube >=0:
        print(guess)
    else:
        print(-guess)



def guessCube(cube):
    epsilon = 0.1
    increment = 0.01
    guess = 0
    while (abs(guess**3-cube) > epsilon): # opp of abs(guess**3 - cube) <= epsilon
        guess +=increment

    if cube>= 0:
        print(guess)
    else:
        print(-guess)


if __name__ == "__main__":
    guess_cube()
