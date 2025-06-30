"""
Comprehensions are a more "pythonic" way(simpler) to create lists, sets, dictionaries by iterating over 
an existing iterable with a condition.
"""
# List comprehensions:
print("List Comprehensions:")
squares = [x**2 for x in range(5)]
print(type(squares)) # list
print(squares)

cubes = [x**3 for x in range(20)]
print(type(cubes)) # list
print(cubes)

test = [2*x for x in squares]
print(type(test)) # list
print(test)

# dictionary comprehensions:
print("Dictionary Comprehensions:")
squared_dictionary = {x:x**2 for x in range(1,101)}
print(type(squared_dictionary))  # dictionary
print(squared_dictionary)

# set comprehensions:
print("Set Comprehensions:")
unique_letters = {cha for cha in "hello world" if cha.isalpha()}
print(type(unique_letters)) # object class of set
print(unique_letters)
print(unique_letters)

# Generator expressions:
"""
Generator expressions are similar to generator object, which is an iterator
that generates values on the fly(lazy). Memory -efficient for large sequences
"""

gen_squares = (x**2 for x in range(100000))
print(type(gen_squares)) # class:generators
print(next(gen_squares))
print(next(gen_squares))

for s in gen_squares:
    print(s)
    if s > 10:
        break
