"""
Lists are stored in contiguous spots in memory 
Lists are mutable
"""

#s1= "racecar"
"""
s1 = "baab"
l1 = list(s1)
half_way = int(len(l1)/2)
print(l1[:len])
print(half_way)
#print(l1[:half_way-1:-1])
#print(l1[:half_way:])
print(l1[:half_way:])
print(l1[:half_way+1:])
print(l1[half_way::])
"""
# ways to create a new list:

testList = list()
testList = []

#Traversing a list:
"""
Same as a string
"""
# Accessing individual elements
"""
Same as a string, but you can actually change the elements in the spot(mutability)
"""

# List Operations:

"""
Works the same ways string operations worked.
"""
# joining of lists: concatenation
# comparing a list:
"""
Python internally individually compares the elements of the lists in lexicographical order. the elements should be of 
comparable types.

python ignores the type( float vs int); as long as they're of comparable types, it's fine

"""
print([1,2,3,45] < [9]) # true as first element in instantly compared, if they're equal, only then will the 2nd element
# be compared

print([2,5] == [2.0, 5.0]) # type ignored

# Working with lists:
import sys

print("Working with lists:\n"+("-"*20)+"\n")
# append( adding to the end)
l1 = list(range(0,11))
print(l1)
print(f"The memory of l1 is {id(l1)}")
print(f"The size of l1 is {sys.getsizeof(l1)}.")
l1.append("balls")
print(l1)
print(f"The memory of l1 is {id(l1)}")
print(f"The size of l1 is {sys.getsizeof(l1)}.")


# deleting a specific index
del l1[0]
del l1[0:len(l1)-5] # dels all but the last 4 elements
print(l1)
print(f"The memory of l1 is {id(l1)}")
print(f"The size of l1 is {sys.getsizeof(l1)}.")

# poping it 
l1.pop() # removes and RETURNS a specific index; by default, it removes the last element
print(l1)
print(f"The memory of l1 is {id(l1)}")
print(f"The size of l1 is {sys.getsizeof(l1)}.")
print("All of the above commands have the same ids.")
print("Done")

# Cloning a list/ Copying a list:
l1 = range(1,11)
l2 = list(l1) # you're making a list on from l1
print(id(l2))
l3 = l2[:] # slicing returns a "copy" in a new memory loc
print(id(l3))
l5 = list(l2) # copied
print(id(l5))
l4 = l2.copy() # copying 
print(id(l4))

# Aliasing a list:
l1 = range(1,11)
l2 = l1 # alias to the same object in memory


# Nested lists and mutability:

"""
Since lists are mutable, mutating nested lists within a list actually changes the 
value of the mutated list in memory.
"""
testList1 = list(range(1,10))
testList2 = list(range(2,5))
testList1.append(testList2) # testList2 is now the last element of testList1
print(testList1)
print(testList2)
testList1[-1][-1] = "This is the last element of testList2"
print(testList1)
print(testList2)
testList3 = "This is a string split into a list.".split()
testList2.append(testList3)
print(testList1)
print(testList2)
print(testList3)
testList1[-1][-1][0] = "This is the first element of testList3"
print(testList1)
print(testList2)
print(testList3)

"""
As you can see, we can mutate many lists from one.
"""
# List Functions and methods:


list1 = list(range(1,11))

list1.index() # returns the first index of value; raises a ValueError if it doesn't exist
list1.append() # adds 1 element to the end of the list
list1.extend() # adds len(value) elements to the end of list, given that value is an iterable
list1.insert() # index, object; inserts object at specified index, moving everyting on the right towards the right 
list1.clear() # clears the list; len(list1) == 0
list1.copy() # returns a copy of the list
list1.count() # counts the no. of occurances of value given
list1.pop() # removes and RETURNS the value at the index given; default last; IndexError otherwise
list1.remove("d") # removes the first occurance of value; ValueError otherwise doesn't return
list1.reverse() # reverses the list in place
list1.sort() # sorts the list in place


# pop vs remove vs del:
"""
remove - value based; 
del and pop - index based

del - based on slicing; returns none
pop - 1 index; default is -1; returns the value
remove - removes the first instance of value; returns none
"""



print(list1)
print(id(list1))
list2 =sorted(list1) # sorted()/ Returns new list; I believe that this isn't a list's method
print(list2)
print(id(list1))
print(id(list2))
del list1 # deletes the object list1