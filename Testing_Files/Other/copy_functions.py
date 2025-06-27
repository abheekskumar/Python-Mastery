import copy 
l1 = list("Hello World.")
# shallow copy:
"""
Creates a new object, but doesn't copy over internal object pointers; they are shared
"""
l2 = copy.copy(l1)

# deep copy:
"""
Creates a new object, copies over the internal structure objects over perfectly
"""
l3 = copy.deepcopy(l2)