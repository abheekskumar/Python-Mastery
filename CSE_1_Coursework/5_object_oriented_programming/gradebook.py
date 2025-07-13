from buildingAClass import *

class Gradebook:
    """ Creates an empty Gradebook"""
    def __init__(self) -> None: # initializing an empty gradebook
        self.students = [] # array to keep track of each student 
        self.grades = {} # dictionary to map grades to each student
        self.isSorted = True # true if self.students is sorted

    def __str__(self) -> str:
        self.sort()
        result = ""
        for studentobj in self.students: # for each student
            result += "{" + str(studentobj.name) +" :" # add full name
            result += str(studentobj.getId()) + ": Grades-"# add id and grades init
            result += str(self.grades[studentobj.id]) # adds all grades 
            result += "}" + "\n"# add newline 
        return result # return one string
    
    def sort(self)-> None:
            """Sorts the internal representation of students by lexigographical order."""
            self.students.sort()
            self.isSorted = True
    # student setter
    def addStudent(self, student:Student) -> None:
        """Adds a student(Of Student type) to gradebook called. Raises an error if student is already in there."""
        assert isStudent(student) , "Incorrect Input"
        assert student not in self.students, f"{student.name} is already in {self.students}"
        self.students.append(student) # add student object to gradebook
        self.grades[student.getId()] = {} # initialize an empty array for storing grades  for that student
        self.isSorted = False # set flag as false
    # student remover
    def removeStudent(self,student:Student) -> None:
        """Removes a student(of type Student) from the called gradebook. Raises an error if student not found"""
        assert (type(student) == Student), "Wrong Input Type"
        assert (student in self.students) , "Student not in this Gradebook"
        self.students.remove(student)
        del self.grades[student.getId()]

    # student getter
    def getStudents(self) -> list:
        """Returns a list of all students."""
        stdnm = []
        for stdobj in self.students:
            stdnm.append(stdobj.name)
        return stdnm
    # grade getter
    def getGrades(self,student:Student,nameFlag = False) -> dict:
        """ Returns all the grades added for a student. Raises an error if student not found."""
        if nameFlag == True:
            assert (type(student) == str), "Wrong Input/ Flag."
            found = False
            for stdobj in self.students:
                if stdobj.name == student:
                    found = True
                    return self.grades[stdobj.getId()].copy()
            if found == False:
                raise NameError(f"{student} isn't in this gradebook") # in case you didn't find, raise an error
            
        assert (type(student) == Student), "Wrong Input/ Flag."
        assert (student in self.students), f"{student} isn't in this gradebook" # in case you didn't find, raise an error
        return self.grades[student.getId()].copy()
    
    # grade setter
    def addGrades(self,student:Student,Subjects:list[str],Marks:list[int]) -> None:
        """Adds grades to grade books under student's ID with the corresponding subjects and marks
        Assumes Subjects and Marks are of iterable type."""
        assert ((type(student) == Student) & (len(Subjects) == len(Marks))), f"Inputs were wrong"
        assert (student in self.students), "Student must already be added to add grades."
        for idx in range(0,len(Subjects)):
            self.grades[student.getId()][Subjects[idx]] = Marks[idx] # adds subjects and corresponding marks
        
    

# s1 = Student("Abheek Satishkumar")
# s2 = Student("George Mason")

# g1 = Gradebook()





# g1.addStudent(s1)
# abh_subjects = ["Physics","Chemistry","Mathematics","English","Computer Science"]
# abh_marks= [95,95,88,95,98]
# g1.addGrades(s1,abh_subjects,abh_marks)

# g1.addStudent(s2)
# grg_subjects = ["Maths","Arts","Science"]
# grg_marks= [95,95,88]
# g1.addGrades(s2,grg_subjects,grg_marks)

# print(g1.getStudents())
# print(g1.getGrades(s1))
# print(g1.getGrades(s2));print(g1.getGrades(s1))


# print("*"*100)
# print("Entire Gradebook:")
# print(g1)

g1 = Gradebook()

s1 = Student("Abheek Satishkumar")
s2 = Student("George Townwell")
s3 = Student("Tomer Grimson")
s4 = Student("Anna Bell")


g1.addStudent(s1)
abh_subjects = ["Physics","Chemistry","Mathematics","English","Computer Science"]
abh_marks= [95,95,88,95,98]
g1.addGrades(s1,abh_subjects,abh_marks)

g1.addStudent(s2)
grg_subjects = ["Maths","Arts","Science"]
grg_marks= [95,95,88]
g1.addGrades(s2,grg_subjects,grg_marks)

g1.addStudent(s3)
abh_subjects = ["Physics","Chemistry","Mathematics","English","Computer Science"]
abh_marks= [36,65,23,55,93]
g1.addGrades(s3,abh_subjects,abh_marks)

g1.addStudent(s4)
grg_subjects = ["Maths","Arts","Science"]
grg_marks= [53,53,23]
g1.addGrades(s4,grg_subjects,grg_marks)


# function to interface with this class and printing the average of each student's grades:

def gradeReport(courseGradebook:Gradebook)-> str:
    """Returns a statement that summarizes the students performance for each Gradebook"""
    result = ["*"*100,f"Grade Report for {courseGradebook}"]
    for std in courseGradebook.getStudents():
        tot = 0
        for grade in courseGradebook.getGrades(std,nameFlag=True).values():
            tot += grade
        try:
            no = len(courseGradebook.getGrades(std,nameFlag=True).values())
            average = tot/no
        except ZeroDivisionError:
            average = 0
        result.append(f"{std} scored an average of {average} over {no} subjects.")
    return "\n".join(result) # adds a newline every element and returns it


print(gradeReport(g1))


