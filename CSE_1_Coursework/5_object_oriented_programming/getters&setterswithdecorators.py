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
        self._age = age
        self._name = None
    def __str__(self):
        return f" {self.name}: {self.age}"
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        if age > 0:
            self._age = age
        else:
            print("Age cannot be negative. Reset to 0.")
            self._age = 0

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name





myanimal = Animal(3)
print(myanimal)
print(myanimal.age)
myanimal.age = 23
print(myanimal.age)
myanimal.name = "Bald"
print(myanimal)

