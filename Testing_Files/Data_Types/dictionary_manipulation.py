"""
Dictionaries are sets with key:value pairs.
they're mutable
they're unordered
they're indexed with key
the key has to be immutable
they aren't a sequence, they're a collection
Keys must be unique
they're internally stored as mappings. that internal function is a hash-function
"""
# making a dict:
firstDictionary = dict() # empty constructor
firstDictionary = {} # 
firstDictionary = {"Abheek":"Likes to swim.","Key":"value"}


firstDictionary = dict([["str","2"],[2,"str2"],[2,"ste3"]])
firstDictionary = dict(zip(["name","salary","age"],[23,234,52])) # zip function implementation for constructing dictionaries


# Mutating a dictionary:
firstDictionary["Abheek"] = "balls"

# adding elements
firstDictionary["New Key"] = 2
secondDictionary = {"balls":1}
firstDictionary.update(secondDictionary) # adds key:value pair from another dictinary
L1 = list(range(0,11))
L2 = list(range(0,11))
L3 = L1,L2
#firstDictionary.update(L1)

# Dictionary operators:

# membership checks only keys, you can use the .values() method to check values


# using other constructs on dictionaries

t1 = tuple(firstDictionary)
s1 = str(firstDictionary) # using constructors for other iterable types on dictionaries builds a
# sequence, for a string, it turns the entire dictionary into a sequence of chars

#iterating over a dictionary:

# over keys:
for i in firstDictionary:
    pass
for i in firstDictionary.keys():
    pass

# over values:
for i in firstDictionary.values():
    pass


# with both key and values:
for k,v in firstDictionary.items(): # this iterates over both the keys and values
    pass

# Other convenienent ways to access/change values:


for key in firstDictionary:
    x = firstDictionary[key] # returns the value associated with key
    print(x)
# if you don't know whether it's in the dictionary, you can do the following:
#
for key in firstDictionary: # iterating over the keys
    x = firstDictionary.get(key,"Default") # this returns the value associated with key, if not found, it returns the default object
    print(x)
"""
In the above cases, it's not really a problem, it's fine. but in some other cases, where you aren't
safely iterating over that, you could use the second method
"""

# Dictionary functions and methods:

print(firstDictionary.pop("balls","return default")) # no last index pop here, mention the key, otherwise, return the return default
print(firstDictionary.clear())
print(firstDictionary.copy())
print(firstDictionary.items())
print(firstDictionary.fromkeys(L1)) # creats a new dict with iterables of keys and values
print(firstDictionary.get("balls","Value")) # this justs RETURNS none if balls isn't found
print(firstDictionary.setdefault("balls","value")) # this SETS the value as "value" if balls isn't found
print(firstDictionary.popitem()) # removes the last entered element 3.7+

# pretty printing dictionaries using json module:

import json
firstDictionary = {'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'cycling']}
print(json.dumps(firstDictionary))
print(json.dumps(firstDictionary,indent =1))
print(json.dumps(firstDictionary,indent = 2))