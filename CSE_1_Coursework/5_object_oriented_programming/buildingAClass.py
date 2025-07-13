import datetime

class Person:
    """Create a person called "name" """
    def __init__(self,name):
        self.name = name
        self.birthdate = None
        self.lastname = name.split(" ")[-1]
    def __str__(self):
        return f"{self.name}: DOB = {self.birthdate}, Lastname = {self.lastname}"\
        
    def __lt__(self,other):
        try:
            assert type(self) == type(other), f"{self.name} and {other.name} must be of Person type"
        except AttributeError:
            raise TypeError(f"{e} was thrown, make sure to use the same type while comparing.")
        if self.lastname == other.lastname:
            return self.name < other.name # compare name if lastnames are equal
        else:
            return self.lastname < other.lastname # otherwise, just return the normal comparison
        
    def setBirthdate(self,year,month,day):
        """Sets the person's birthdate."""
        self.birthdate = datetime.datetime(year,month,day)
    def getLastName(self):
        "Returns the person's last name"
        return self.lastname
    def getBirthdate(self):
        """Returns the person's birthdate."""
        return self.birthdate
    def getAge(self):
        """Returns the person's age."""
        return datetime.datetime.today() - self.birthdate
    
    

p1 = Person("Abheek Satishkumar")
p1.setBirthdate(2006,7,3)
p2 = Person("George Allis")


personList = [p1,p2]

# print(p1 > p2)
# print(p1.getBirthdate())
# print(p1.getLastName())
# print(p1.getAge())


# for person in personList:
#     print(person.name)

# personList.sort()
# for person in personList:
#     print(person)

class MITPerson(Person):
    """Creates an MITPerson Object with name."""
    #inherits everyother function from person
    id = 1
    def __init__(self,name):
        Person.__init__(self,name) # sets name and initializes lastname, DOB
        self.id= MITPerson.id
        MITPerson.id +=1

    def getId(self):
        """Returns MITPerson's ID"""
        return self.id
    
    def speak(self,utterance):
        """Speaks utterance"""
        return f"{self.name} says \"{utterance}\""
    
    def __lt__(self,other):
        assert type(self) == type(other), "Types must be the same"
        return self.id < other.id # just id numbers comparison


p3 = MITPerson("Eric Professor")
p4 = MITPerson("Ana Bell") 

MITPersonList = [p3,p4]
# print(p3.speak("Hello"))

# print(p3.getId() ,p4.getId() )
# print(p3 < p4) # calls MITPerson __lt__ method as: p3.__lt__(p4)
# print(p1 < p4) # calls person __lt__ method as it's the first one: p1.__lt__(p4)

# for mitperson in MITPersonList:
#     print(mitperson)
# MITPersonList.sort()
# for mitperson in MITPersonList:
#     print(mitperson)
class Student(MITPerson):
    pass


class UG(Student):
    """Creates a Undergraduate instance, inherited from MITPerson"""
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year = classYear
    def getClass(self):
        return self.year
    def speak(self,utterance):
        return MITPerson.speak(self,"Yo bro, "+ utterance)
class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj,Student) # returns true if obj is in atleast student or one of it's sub classes
"""
isinstance(obj,[class or tuple]) checks if obj is an instance of a particular class or any of it's subclasses.
"""

s1 = UG("Matt Damon",2017)
s2 = UG("Ben Affleck",2017)
s3 = UG("Lin Manuel Miranda",2018)
s4 = Grad("Leonardo di Caprio")

studentList = [s1,s2,s3,s4]

# print(s1)
# print(s1.getClass())
# print(s1.speak("Where is the quiz?"))
# print(s2.speak("I have no idea"))
# print(isStudent(s1)) # returns true


class Professor(MITPerson):
    def __init__(self,name,department):
        MITPerson.__init__(self,name)
        self.department = department
    def speak(self,utterance):
        return MITPerson.speak(self,f"in the course {self.department}, we say:" + utterance)
    def lecture(self,topic):
        return self.speak("It is obvious that"+topic)
    
# faculty = Professor("Doctor Arrogant","CSE")
# print(faculty.speak("I don't care about your existence."))

    

    

    
