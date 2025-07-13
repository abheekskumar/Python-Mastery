print("*"*200)
print("Exercise 3:")
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def getDescription(self):
        return "This charm summons an object to the caster, potentially over a significant distance."

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo()) # look at how this calls and eventually prints get descriptions
# look at how it's passed into the spell __str__ method



print("*"*200)
print("Exercise 4:")


"""
Multiple classes resolution:
look at object D, it inherits from 2 classes. In this case:
Python uses a left to right, depth first search which moves through the entire class hierarchy.(I.E, moving
through all the superclasses).
hence, it checks all the way up for C and then, for B
"""

class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")


obj = D()
"""D → C → B → A → object"""
print(obj.a) # 2
print(obj.b) # 3
print(obj.c) # 5
print(obj.d) # 6
obj.x() # A.x
obj.y() # C.y
obj.z() # D.z