"""
# getters and setter should be used outside the class to access data attributes, inside, we traditionally 
# directly use the data representation.


We do this information hiding to separate interfaces of the the classes with it's implementation.
That implementation might also change later on, in that case, it would be better to have getters and setters

Python also has another way of handling this with decorators
you can set them with @property(for the getter itself) and @age.setter(for the setter)
for implementations like:
x.age = 23 (calls the setter)
print(x.age) (calls the getter)

You can "hide"(soft hiding) the name of a var with
class Person:
    def __init__(self,age):
        self.__age = age
        (python renames this to self._Person_age), which makes it harder to access and accidently break.


Subclasses can have same method names as superclass.
Subclasses can have same method names as other subclasses.

Methods are only accessed from a particular class or higher up, not OTHER classes
at the same level.


"""




class Animal(object):
    """Creates an instance of an Animal."""

    def __init__(self,age): # input what data is used for initializing an animal
        self.age = age # initialize each instance with the age parameter that was passed in
        self.name= None # initialize every instance with another attribute that isn't passed in
    def __str__(self):
        return "Animal:"+str(self.name)+":"+str(self.age)
    
    # Getter
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    
    # Setter
    def set_name(self,newname = ""):
        self.name = newname
    def set_age(self,newage):
        self.age = newage


myanimal = Animal(3)
print(myanimal)
print(myanimal.get_age())
myanimal.set_age(23)
print(myanimal.get_age())
