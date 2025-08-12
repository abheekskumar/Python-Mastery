"""
Instance Variables
- created for each instance
- vars are created in __init__


Class Variables
- vars that are defined in class, but not in __init__
- belongs to a class, shared with all the instances of that class
- Accessed with <class_name>.<var_name>
"""

from hierarchies import Animal

class Rabbit(Animal):
    tag = 1# defined outside the init dunder block
    def __init__(self,age,parent1=None,parent2=None):
        self.age = age
        self.parent1 = parent1
        self.parent2 = parent2
        self.id = Rabbit.tag # accessed with the . notation w/ class name
        Rabbit.tag +=1 # augmented operation to increment the tag
    # def __rfinder__(selfrid):
    def __add__(self,other): # adding a function for parents, mapping with IDs.
        assert ((type(self) == type(other)) & (type(self) == Rabbit)), "Mating is only for the same species."

        return Rabbit(0,self.get_rid(),other.get_rid())

    def get_rid(self):
        return int(str(self.id).zfill(3)) # z fill pads w/ 0s, but only on a str
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    

peter = Rabbit(2)
Hopsy = Rabbit(3)
peter.set_name("Peter")
Hopsy.set_name("Hopsy")
Mopsy = peter + Hopsy
Mopsy.set_name("Mopsy")
print(Mopsy);print(peter);print(Hopsy)
print(Mopsy.get_parent1(),Mopsy.get_parent2())


print("*"*200)
print("using == with rabbit")


class Rabbit(Animal):
    tag = 1# defined outside the init dunder block
    def __init__(self,age,parent1=None,parent2=None):
        self.age = age
        self.parent1 = parent1
        self.parent2 = parent2
        self.id = Rabbit.tag # accessed with the . notation w/ class name
        Rabbit.tag +=1 # augmented operation to increment the tag
    # def __rfinder__(selfrid):
    def __add__(self,other): # adding a function for parents, mapping with IDs.
        assert ((type(self) == type(other)) & (type(self) == Rabbit)), "Mating is only for the same species."

        return Rabbit(0,self,other)

    def get_rid(self):
        return int(str(self.id).zfill(3)) # z fill pads w/ 0s, but only on a str
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2    
    
    def __eq__(self,other):
        parents_same = (self.parent1.id == other.parent1.id) & (self.parent2.id == other.parent2.id)
        parents_opp = (self.parent1.id == other.parent2.id) & (self.parent2.id == other.parent1.id)
        return parents_same or parents_opp
    

peter = Rabbit(2)
Hopsy = Rabbit(3)
peter.set_name("Peter")
Hopsy.set_name("Hopsy")
Mopsy = peter + Hopsy
Mopsy.set_name("Mopsy")
print(Mopsy);print(peter);print(Hopsy)
print(Mopsy.get_parent1(),Mopsy.get_parent2())


cotton = Rabbit(1,peter,Hopsy)
print(Mopsy==cotton)