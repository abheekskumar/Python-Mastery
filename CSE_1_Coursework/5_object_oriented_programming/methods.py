"""
All methods have self passed as an argument
there are a few special methods(procedural attributes) specified below
"""
class Coordinate(object):
    def __init__(self,a,b): # a and b are passed in, x and y are mapped
        self.x = a
        self.y = b
    
    def distance(self,other):
        xDistSq = (self.x - other.x)**2
        yDistSq = (self.y - other.y)**2
        return((xDistSq + yDistSq)**0.5)
    
"""
two ways of using methods:
"""
print("*"*100)
print("Invoking methods different ways")
C = Coordinate(10,10) # Coordinate C
O = Coordinate(0,0) # Origin

print(C.distance(O))
"""
If the method is called on an instance, the self is mapped to that instance and other to the other
argument passed in
"""
print(Coordinate.distance(C,O))
"""
If the method is called on the class itself, the self is mapped to the first argument and other is mapped
to the second argument

What's important to remember is when you have to pass in the self(calling on the class method) 
and when python automatically maps it(calling on the instance method)
"""

"""
When you use Coordinate.distance(C,O),
Coordinate refers to a frame within which the method distance is looked up and reqires 2 arguments

When C.distance(O) is used,
C points to the frame within which self is already assigned, the .distance here
points to this frame. In this frame, self(as said above) is already assigned and .distance
only needs 1 argument.
"""


# Printing instances/objects
print("*"*100)
print("Printing instances cleanly using __str__ method:")
print(C) # prints class and mem address of where it's stored not usefull

class Coordinate(object): # redefining a class works
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self): # special method that's invoked when print() is called on an instance
        return ("<"+str(self.x)+","+str(self.y)+">") # must return a string object


C = Coordinate(10,10)
print(C) # prints out using the __str__ special method

# no __add__ method defined:
#X = C + O returns an error 
#print(X)
# error:
#print(len(C))



# Types vs Classes
print("*"*100)
print("Types v/s Classes:")
print(type(C)) # C points to a frame of the Coordinate class
print(Coordinate,type(Coordinate)) # Coordinate points to a global class with type "type"(python object)


print(isinstance(C,Coordinate)) # built in function that returns a bool if an 
# object is an instance of a class/tuple


# Common special methods:
class Coordinate(object):
    """Creates a 2D Coordinate System with basic methods."""
    def __init__(self,x,y): # used for initializing new instances
        self.x = x
        self.y = y
    def __str__(self): # used for print(instance)
        return ("<"+str(self.x)+","+str(self.y)+">")
    def __add__(self,value): # used for instance + value
        return Coordinate(self.x+value.x,self.y+value.y) # returns new Coord object
    def __sub__(self,value): # used for instance - value
        return Coordinate(self.x-value.x,self.y-value.y) # returns new Coord Object
    def __len__(self): # used for len(instance)
        return 2 # just a placeholder

    def __eq__(self, value): # used for instance == value
        return ((self.x == value.x) & (self.y == value.y)) # returns bool
    def __ne__(self,value): # not equal to !=
        pass
    def __lt__(self,other): # "less than" < OR can work the other way too???
        return ((self.x < other.x) & (self.y < other.y))
    def __le__(self,other): # "less than equal to" <=
        pass
    def __gt__(self,other): # "Greater than" >
        pass
    def __ge__(self,other):# "Greater than equal to" >=
        pass

    
    

C = Coordinate(10,200)
O = Coordinate(0,0)


print("*"*100)
print("Special methods")
X = C + O
print(X) # __add__ works as implemented
X = O - C
print(X) # __sub__ works as implemented
print(len(X)) # __len__ works as implemented
print(C == O) # __eq__
print(C<O) # __lt__ works as expected



