import random as rd
# radom:
x = rd.random() # generates a float within the interval [0.0<=N <1.0); no arguments

# randint:
x = rd.randint(5,23) # generates an int within the inter [a<=N<=b]
x = rd.randint(0,100-1)+ rd.random() # to generate a floating point from 0 to 100
x = rd.randint(0,100) # to generate a percent value


# randrange:
x = rd.randrange(35) # generates a random int from 0 to 35 (both inclusive)
x = rd.randrange(2,62) # generates a random int from 2 to 62
x = rd.randrange(2,52,6) # step value of 6, internally generates a structure with that and then chooses randomly
print(x)


