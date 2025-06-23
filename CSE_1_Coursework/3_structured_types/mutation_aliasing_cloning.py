# Lists are mutable; It's essentially an object in memory, to which a variable points torwards
# you can have multiple vars(pointers in python) pointing to the same object

l1 = list(range(1,11)) # this is a list
l2 = l1 # points to same memory, l2 is known as an alias

l3 = list(l2) # this makes a copy of l2(which points to the same list as l1) at this
# point of time in flow of control

print(l1)
print(l2)
print(l3)
print(id(l1))
print(id(l2))
print(id(l3)) # this prints a different vir address than the 2 above statements, even though all of them 
# have the same elements

# is vs == : 
# == checks value, is checks memory
if l1 is l3:
    print("L1 IS L3")

if l1 == l3:
    print("L1 == L3")



"""
Nested Lists
if you append a list to a list, you can mutate like hell
be careful whenever you're changing values; think of all of them as pointers to 
objects in memory
"""

warm = list(("yellow","Orange"))
hot = "red".split()
brightColors = list()
brightColors.append(warm)
brightColors[0][1] = "test"

print(warm)
print(hot)
print(brightColors)
print(id(warm))
print(id(hot))
print(id(brightColors))