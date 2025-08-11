"""
Dictionaries are sets with key:value pairs.
they're mutable
they're unordered
they're indexed with key
the key has to be immutable
they aren't a sequence, they're a collection
Keys must be unique


they're internally stored as mappings in a hash table.
that table is indexed with hashkeys, generated with a hash function.
each element MAY NOT have a unique hash key as that's very space inefficient.
for most cases, the size of a hash table is sufficient to accomodate all the keys, if not, there's going
to be some keys with collisions.
Hash collisions are allowed- 2 keys may share the same hash key/index, in which case resolution must take place:

"""

# Hashing in a dictionary
hashTableSize = 5 # hypothetical
# suppose you're using indexing 3 values in this example dictionary
exampleDictionary = {"cat":23,"ball":24,"test":26}
# the hash function determines the relation between a key and it's corresponding value
# this key is then translated into an integer
c1 = hash("cat")
c2 = hash("ball")
c3 = hash("test")
print(c1,c2,c3) # hashes
# hash conversion based on table size:
c1Int = c1%hashTableSize
c2Int = c2%hashTableSize
c3Int = c3%hashTableSize
print(c1Int,c2Int,c3Int) 
# these values are then stored in a hash table and used to index the values
# as you can see, 2 of them have the same value, a collision would occur in this case


# making a dict:
firstDictionary = dict() # empty constructor
firstDictionary = {} # 
firstDictionary = {"Abheek":"Likes to swim.","Key":"value"}


firstDictionary = dict([["str","2"],[2,"str2"],[2,"ste3"]])
firstDictionary = dict(zip(["name","salary","age"],[23,234,52])) # zip function implementation for constructing dictionaries
# zip takes in 2 iterables and returns 1 consisting of the pairs for corresponding elements.
# dict constructor acting an an iterable where each element is a collection(list,tuple) itself will
# turn that colletion into key:value pairs.




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

t1 = tuple(firstDictionary) # over the keys
print(t1)
s1 = str(firstDictionary) # using constructors for other iterable types on dictionaries builds a
# sequence, for a string, it turns the entire dictionary into a sequence of chars
print(s1)

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


# for key in firstDictionary:
#     x = firstDictionary[key] # returns the value associated with key
#     print(x)
# # if you don't know whether it's in the dictionary, you can do the following:
# #
# for key in firstDictionary: # iterating over the keys
#     x = firstDictionary.get(key,"Default") # this returns the value associated with key, if not found, it returns the default object
#     print(x)
"""
In the above cases, it's not really a problem, it's fine. but in some other cases, where you aren't
safely iterating over that, you could use the second method
"""

# Dictionary functions and methods: 

print(firstDictionary.pop("balls","return default")) # no last index pop here, mention the key, otherwise, return the return default
print(firstDictionary.popitem()) # removes the last entered element 3.7+

# print(firstDictionary.clear())
# print(firstDictionary.copy())

print(firstDictionary.items())

print(firstDictionary.fromkeys(L1, "Default Values")) # creats a new dict with iterables of keys and values
# it's an class method, not an instanceone
# print(dict.fromkeys(L1,"Default Values")) #results in the same

# print(firstDictionary.get("balls","Valu3")) # this justs RETURNS none if balls isn't found
# print(firstDictionary.setdefault("balls","value")) # this SETS the value as "value" if balls isn't found
# print(firstDictionary.get("balls","Valu3"))

# pretty printing dictionaries using json module:

import json
# firstDictionary = {'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'cycling']}
# jsString = json.dumps(firstDictionary) # this is a string that can be parsed into JSON objects
# print(jsString, type(jsString)) # this is a string 
# # print(json.dumps(firstDictionary,indent =1))
# # print(json.dumps(firstDictionary,indent = 2))
# secondDictionary = json.loads(jsString)
# print(secondDictionary,type(secondDictionary))