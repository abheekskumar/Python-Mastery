"""
Python strings are stored in memory by storing individual chars in contiguous memory spots
"""


# ways to create a new string:
s1 = str()
s1 = ""
#...
s1 = "Hello World! This is Abheek Satishkumar."
# String traversal:
for char in s1: # traversing over each character
    pass
for idx in range(len(s1)): # traversing over each index
    pass
for idx in range(-1,-len(s1)-1,-1): # reversing a string by negative indexing
    print(s1[idx])

# traversal with enumerate:
for idx, ele in enumerate(s1):
    print(f"{idx}:{ele}")
# String Operators:

    # concatenation
s2 = s1 + s1
print(s2)
    # replication
s2 = s1*3
print(s2)
    # comparison
"""
    for equality and nonequality, it's easy because it compares each character individually
    with less than and greater than:
    It compares the unicode representation(ordinal values)
    note:
        "s" > "S" as unicode representation of "s" is higher
    it's: DIGITS -> uppercase -> lowercase

"""
print("abc"> "ABC") 
print(ord("a")) # ord to attain the ordinal(unicode) representation
print(ascii(ord("a"))) # ascii to attain the the char from the ord

# String indexing

"""
you cannot index out of bounds( it'll return an error)
"""
print(s1[0])
# due to immutability, you cannot reassign chars

# String Slices
"""
It's a part of the string containing some contiguous characters
you can slice out of bounds(it won't return an error)

"""
print(s1[0:1000000000]) # no error
# print(s1[])

s2 = s1 [0:3] # [)- first index is included, the second index is excluded; it returns a string
print(s2)
# This is reassignment, not mutation since string in immutable
s1 = s1[0:34]
print(s1) 
# for negative slicing:
print(s1[0:-1]) # the -1 is not actually included, if you want to inlucde it:
print(s1[0:]) # this includes all chars
print(s1[::-1]) # to reverse a string
print(s1[0:len(s1):-1],"CHECK THIS") # return nothing it cannot traverse that with a -1 step
print(s1[-1:-(len(s1))-1:-1]) # to replace s1[::-1]
print("\n")
print(s1[:234]+s1[234:]) # 234 is literally out of bounds s1[:n] + s1[n:] returns the original string
print()
print(s1[0:235234]) # no error




s1 = "Hello World! This is a string."
l1 = list(s1) # converting a string to a list of CHARACTERS


# Split: called on a string, converts a string into a list based on argument given
l2 = s1.split() # converting a string to a list of WORDS
# l3 = s1.split("") # not allowed, use list(string) to obtain a list of characters.

# Join: called on a string instance, takes in a list as an attribute, converts 
# a list into a string
s2 = "".join(l1) # converting a list of CHARACTERS to a string using an empty string
s3 = " ".join(l2) # converting a list of WORDS to a string using a whitespace

print(s1,l1,l2,s2,s3,sep = "\n")


# String functions and methods

s1 = "Hello world, this is Abheek Satishkumar!"
s2 = "This is string number two."
s3 = "This is string number three."
# print("1".isascii())
# s1.index(str) # returns the first instance where substring str is found ; if not throws ValueError
# s1.find(str) # retunrs the first instance where substring str is found; if not -1
# s1.count(str) # returns the no. of times substring str was non-overlapping
s1.encode() # prefixes the string with "b"


s1.startswith(str,tuple) # returns True if string starts with substring str or a tuples of substrings; false otherwise
s1.endswith(str,tuple) # returns True if string ends with substring str or a tuple of substrings; false otherwise

s1.strip(char) # returns copy of s1 with leading and trailing "char" removed; default whitespace
s1.lstrip(char) # leading
s1.rstrip(char) # trailing

"str".join(iterable) # inserts the strings' whose method was called inbetween the iterables 
s1.split(str) # returns a list of stubstings- s1 split at "str"; default: whitespaces, newlines, and other escape sequences
s1.splitlines() # retunrs a list of lines in the string, argument keepends defaults to false(line breaks aren't included) and vice versa

s1.isalnum()# returns true only if s1 has alphabets AND numerics
s1.isalpha() # retunrs true if s1 has only alphabets
s1.isascii() # reutnrs true if all of s1's characters are ascii characters
s1.isdecimal() # retunrs true if all of s1's characters are base ten numbers
s1.isdigit() # retunrs bool depending on whether 
s1.islower() # retunrs bool depedning on whether all lowercase
s1.isnumeric() # retunrs bool depending on all the characters are nubmers
s1.isprintable() # retunrs true 
s1.isidentifier() # if s1 is a var(identifier)
s1.istitle() # if s1 is titular

s1.capitalize() # retunrs a new string that is capitalized( first char uppercase, rest lower)
s1.title()# returns a new string that is titularized
s1.swapcase() # retunrs a new string of chars with case swapped

s1.lower() # returns a new string of all lowercase chars
s1.upper() # retunrs a new string of all chars uppercase

