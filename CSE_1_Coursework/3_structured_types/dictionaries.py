# info is stored across lists in different places

names = [] # list of names
grades = [] # list of grades
courses = [] # list of courses

# Dictionaries- we can create mapping
"""
key:value pairs, the indexes are customized. The "key" type should be immutable, 
    the value can be mutable.
Dictionaries are mutable, you can add in entries, edit them, remove them.
Don't rely on the order of dictionaries, it's generally a set(unordered data strucutre)
The values can be anything, other sequences, duplicates..
The keys should be immutable, unique. More specifically, they need to be hashable( learn about this later)

Diff b/w list & dict:
list is ordered, therefore check index
dict is unordered, therefore "lookup"
"""

dictOne = {}

grades = {'Key 1':"Value 1","Key 2":"Value 2"}

print(id(grades))
print(grades)
print(grades["Key 1"])

grades.keys() # method of dictionary that generaates an iterable
grades.values() # method of dictionary that generates an iterable