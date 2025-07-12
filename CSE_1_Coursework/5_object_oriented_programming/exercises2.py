class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self,other):
        assert type(self) == type(other), f"{self} and {other} aren't of the same type."
        if ((self.getY() == other.getY())&(self.getX() == other.getX())):
            return True
        return False
    def __repr__(self):
        result = "Coordinate(%d,%d)" % (self.getX(),self.getY()) # creates a string w/ all the relevant info
        return result
    

O = Coordinate(0,0)
print(O)

x = repr(O) # creates an input string in such a way  that it would be possible to create the same object
# when evaluated
print(x) # string
print(type(x)) # string

origin = eval(x) # eval runs whatever that input string was
print(origin,type(origin))

print(origin == O)

print("*"*100)
print("Other Example:")

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        """Returns len of object"""
        return len(self.vals)
    def intersect(self,other):
        assert type(self) == type(other), f"Types of {self} and {other} are mismatched."
        t = intSet()
        for ele in self.vals:
            if other.member(ele):
                t.insert(ele)
        if len(t) ==0:
            raise ValueError(f"{self} and {other} have no elements in common")
        return t




a = intSet(); b = intSet()
a.insert(1);a.insert(2)
b.insert(3); b.insert(2)

print(a);print(b)
c = a.intersect(b)

print(c)
        