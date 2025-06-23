#s1= "racecar"
"""s1 = "baab"
l1 = list(s1)
half_way = int(len(l1)/2)
print(l1[:len])
print(half_way)
#print(l1[:half_way-1:-1])
#print(l1[:half_way:])
print(l1[:half_way:])
print(l1[:half_way+1:])
print(l1[half_way::])"""

# Cloning a list/ Copying a list:
l1 = range(1,11)
l2 = list(l1) # you're making a list on from l1
l3 = l2[:] # slicing returns a "copy"

# Aliasing a list:
l1 = range(1,11)
l2 = l1 # alias to the same object in memory

# List Functions:



list1 = list(range(1,11))
list1.reverse()
list1.sort() # sort()/ Mutates list in place
print(list1)
print(id(list1))
list2 =sorted(list1) # sorted()/ Returns new list
print(list2)
print(id(list1))
print(id(list2))
