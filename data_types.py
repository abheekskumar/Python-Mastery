# Data Types

# strings  immutable
string1 = "This is a string."

string2 = string1[-1:-len(string1):-1]
string2.removesuffix("string.")
print(string2)

# lists mutable
list1 = [1,2,"this is a string too"]
list1 = [52] + list1
list1.extend({2,5})
list1.pop()
print(list1)
print()

# dictionaries mutable unordered
dict1 = {"key1":2,"key2":3}
print(dict1.pop("key1"))
print(dict1)

# tuples immutable, ordered, non unique
tuple1 = 2,
print(type(tuple1))
print(len(tuple1))
print(tuple1)


# sets mutable, unordered, unique
set1 = {1,2,34}
print(set1)






# identifiers variable names
num1 = 2
x = 234
y = 33.4
u = complex(3,2)
print(u.__class__)
print(type(u))
print(id(u))



# keywords
import math
import random
print(random.random())
x = list(range(5))
print(x)
print(random.randint(1,6))
print(math.pi)



# Literals/ values
print(type(complex(2,5)))
bool()
float()
str()
int()
list()
dict()
tuple()
set()



# operators
def main2():
    import inspect
    pass
    print(__name__)
    print("lmao")
    print(inspect.currentframe)
print(__name__)
if __name__ == "__main__":
    main2()