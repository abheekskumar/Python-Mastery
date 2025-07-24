import module_test as mt # importing a python file as such
# access functions and vars with mt.<name>
print(mt.x)
print(mt.returnSquare(mt.x))



from module_test import * # imports into current namespace
# access directly
print(x)
print(returnSquare(x))



## package testing
"""
For python to recognize a package, it needs to have a __init__.py file inside the folder
"""
from package_testing import packageModule1 as pm1

# print(pm1.memoFib(pm1.test))


