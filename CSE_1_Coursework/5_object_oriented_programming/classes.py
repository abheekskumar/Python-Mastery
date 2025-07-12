"""class header/definition: class [class name](class parent):
the current class inherits all the methods and data attributes from the parent class
The word object signifies that Coordinate is a python object and inherits all its attributes
It is said that Coordinate is a sub-class of object and that Object is a superclass of Coordinate
"""
class Coordinate(object):
    """
    Attributes of a class:
    data and procedures(methods) that belong to that class

    2 Type of attributes:
    Data Attributes - data that makes up the class
    Method / Procedures Attributes - function/ proceude  that make sense to be
             implemented only for this class
    """

    """
    special __init__ method specifies how to create instances of that object
    self here points to that instances itself
    the .x .y methods "bind" the variables(x and y) passed in to that instance
    """
    def __init__(self,x,y): # double underscore is referred to as dunder
        self.x = x
        self.y = y

    """distance is a procedural method that defines how that defines what each instance
    will do with the distance method."""

    def distance(self,other):
        """ here other refers to another instance of this class"""
        x_sq = (self.x - other.x)**2
        y_sq = (self.y - other.y)**2
        return ((x_sq+y_sq)**0.5)
    

    def swap(self): 
        """ no other parameter defined, hence only operates on self"""
        self.x,self.y = self.y,self.x
        
""" 
Creating instances "c"(2,4 passed as vars) and "origin"(0,0 passed as vars) of that class.
This calls the __init__ method to create an instance
each instance creates its own frame within which the x and y values are bounded.
think of this frame as it's own scope
x of one instance is different from the x of the other instance.
"""
c = Coordinate(2,200)
origin = Coordinate(0,0)
print(c.x,c.y)
print(origin.x)
print(c.distance(origin))

c.swap() # no object passed in
print(c.x,c.y) # swapped

c.swap()
print(c.x,c.y)



"""
Note:
the "." notation is used to reference an attribute of that class
instance.something - data attribute
instance.something() - procedural attribute that is "callable"
"""