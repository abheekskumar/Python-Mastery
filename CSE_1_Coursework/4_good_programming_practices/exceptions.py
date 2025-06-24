"""
Exceptions & Assertions:

Exceptions - to anticipate an unexpected condition
What to do when you encounter an error:
Don't fail silently, you can use default values, but let the user know what is going on.

use try-except clause to deal with exceptions
the try-except also has a finally clause that occurs always(whether there is or there isn't an error)
you can have seperate except clauses for different exceptions
"""
# basic handling of exceptions:
def basicHandlingOfExceptions():
    try:
        n1 = int(input("Enter the first number:"))
        n2 = int(input("Enter the second number:"))
        ans = n1/n2
        print(f"{n1}/{n2} is equal to {ans}")
    except ZeroDivisionError: # to handle division error
        print("Cannot divide by 0!")
    except ValueError: # to handle improper inputs
        print("Please put in proper inputs!")
    except: # to handle all other exceptions(default exception)
        print("Other exception has been hit.")
    else: # executes when there is no exception thrown
        pass
    finally: # always executed no matter what
        pass

# Keep asking the user for valid input
def persistent_input():
    while True: # keeps asking until we get valid input
        try:
            n = int(input("Please enter an integer:"))
            break # throws us out of while loop
        except ValueError: # this is hit if line 32 raises an error
            print("Input is now an integer; Try again!")
    print("Correct input of an integer!")

def control_input():
    # Control input:
    data = []
    file_name = input("Provide a name of a file of data.")

    try:
        file_handle = open(file_name,"r")
    except Exception as e: # only an IO Error can be hit
        print(f"{e} has been thrown.")
        print("Please enter a valid file name!")
    else: # if no exceptions are thrown
        for new in file_handle:
            if new != '\n':
                addIt = new[:-1].split(",")
                data.append(addIt)
        file_handle.close()

    gradesData = []
    try:
        for student in data:
            try:
                name = student[0:-1] # everything but the last one
                grades = int(student[-1]) # this will throw a value error if grade was missing
                gradesData.append([name,grades])
            except ValueError: # to deal with missing grade
                gradesData.append([student[:],[]])
    except:
        print(Exception)


# exceptions as control flow:
"""
Used to raise an exception when unable to produce a result consistent with function's specification
with the syntax:
raise <exceptionName>(<arguments>)
ex: raise ValueError("Something is wrong")
"""
def exceptions_as_control_flow():
    def get_ratios(L1,L2):
        """
        ...
        """
        ratios = []
        for index in range(len(L1)):
            try:
                ratios.append(L1[index]/float(L2[index]))
            except ZeroDivisionError:
                ratios.append(float("NaN")) # NaN- Not a number Python special character
            except: # for any other exception thrown
                raise ValueError("get_ratios called with bad arg") # you define what the interpreter tells the console
            # this is used to raise one's own error message.
        return ratios
    # -------
    L1 = [1,2,3,4]
    L2 = [5,6,7,8]
    L3 = [5,6,7,]
    L4 = [5,6,7,0]

    print(get_ratios(L1,L4))

def exceptions_as_control_flow_2():
    def get_stats(class_list):
        new_stats = []
        for elt in class_list:
            new_stats.append([elt[0],elt[1],avg(elt[1])])
    
    def avg(grades):
        try:
            return ((sum(grades))/(len(grades)))
        except:
            print("No Grades Data. 0 being input") # notifying the user
            return 0 # 0 being inserted instead

    #---

    L = [[["peter","parker"],[80,70,85],["bruce","wayne"],[100,80,74]]]
    get_stats(L)


if __name__ == "__main__":
    exceptions_as_control_flow_2()
    pass
