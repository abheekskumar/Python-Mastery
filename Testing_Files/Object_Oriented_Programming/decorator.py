
# @static methods:

print("*"*100,"@static method:",sep = "\n")
class Math:
    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def multiply(x,y):
        return x*y
    @staticmethod
    def divide(x,y):
        return x/y
    @staticmethod
    def remainder(x,y):
        return x%y
    @staticmethod
    def floor_division(x,y):
        return x//y

x = 25
y = 234

print(Math.add(x,y))
    


# @property:
print("*"*100,"@property:",sep = "\n")
class Circle:
    def __init__(self,radius): # private  
        self._radius = radius

    @property # property allows us to access the name of the method without calling the method
    def radius(self):
        """Gets the radius of the circle."""
        return self._radius
    
    @radius.setter
    def radius(self,value):
        """Set the radius of the circle."""
        if value >= 0:
            self._radisu = value
        else:
            raise ValueError("Radius must be positive.")
        
    @property
    def diameter(self):
        """Get the diameter of the circle."""
        return self._radius*2

c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 10
print(c.radius)
print(c.diameter)
# c.diameter = 23 # no setter property so it results in an error

# classmethod
print("*"*200,"@classmethod:",sep = "\n")
class Person:
    species = "Homo Sapiens"
    def __init__(self,test):
        self.test = self.species
    @classmethod
    def get_species(cls):
        return cls.species
    
    def get_name(self):
        return self.get_name

print(Person.get_species())
print(Person.species)
p = Person(x) # instance of the class
print(p)
