import random



class Animal:
    """Creates an instance of an Animal."""

    def __init__(self,age): # input what data is used for initializing an animal
        self.age = age # initialize each instance with the age parameter that was passed in
        self.name= None # initialize every instance with another attribute that isn't passed in
    def __str__(self):
        return "Animal:"+str(self.name)+":"+str(self.age)
    
    # Getter
    def get_age(self):
        """Returns age of animal."""
        return self.age
    def get_name(self):
        """Returns name of animal."""
        return self.name
    
    # Setter
    def set_name(self,newname = ""):
        """Sets name of animal"""
        self.name = newname
    def set_age(self,newage):
        """Sets name of animal"""
        self.age = newage

class Cat(Animal):
    # every attribute is inherited from Animal
    def speak(self): # addes new functionality
        print("Meow!")
    def __str__(self): # overrides the previsou __str__ definition 
        return "Cat:"+str(self.name) + ":" + str(self.age)
    
class Rabbit(Animal):
    def speak(self):
        print("Meep")
    def __str__(self):
        return "Rabbit:" + str(self.name) + ":" + str(self.age)
class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age) # uses Animal;s constructor to set age 
        Animal.set_name(self,name) # uses Animal's set_name method to set name
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self,other):
        """Returns the age difference between self and other."""
        assert type(self) == type(other) , "Type mismatch"

        #diff = self.age - other.age
        diff = self.get_age() - other.get_age() # alternative with getters from Animal's definition.
        if diff > 0:
            print("Age Difference:",diff)
        else:
            print("Age Difference:",-diff)
class Person_copy(Person):
    pass # inherits everythin from Person and doesn't add/overwrite something

class Student(Person):
    def __init__(self,name,age,major=None): # initiailze a student
        Person.__init__(self,name,age) # use Person's constructor, which uses animal constructor
        self.major = major
    def change_major(self,newmajor):
        self.major = newmajor
    def speak(self):
        r = random.random()
        if (r<0.25):
            print("I have homework.")
        elif (r<0.5):
            print("I need sleep.")
        elif (r < 0.75):
            print("I should eat.")
        else:
            print("I am watching TV.")
    def __str__(self):
        return "Student:"+str(self.name)+":"+str(self.age) + ":"+str(self.major)





    
jelly = Cat(1)
print(jelly.get_name())
jelly.set_name("JellyBelly")
print(jelly) # uses cat's __str__ definition
print(Animal.__str__(jelly)) # uses Animal's __str__ definition


blob = Animal(1)
print(blob)
blob.set_name()
print(blob)
jelly.speak()
Peter = Rabbit(23)
Peter.speak()

#blob.speak() Error since speak isn't from Animals


pa = Person("George",23)
pb = Person("Elizabeth",26)


Person.age_diff(pa,pb) # same thing called differently
pa.age_diff(pb) # ""
Cat.speak(pa)# Just prints that, does nothing with self
print(Cat.__str__(pa)) # passes a person into Cat's __str__ and only uses that.
