class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = "10:30"
        print(self.time)

clock = Clock('5:30')
clock.print_time() # prints the instace attribute, not local var created



class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self,time):
        print(time)

clock = Clock('5:30') # sets instance.time as 5:30
clock.print_time('10:30') # just prints in the passed var, nothing to do with the actual instance


class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30') # creating an object
paris_clock = boston_clock # same object
paris_clock.time = '10:30' # change instance attribute
boston_clock.print_time() # invoke a method that prints that built in attribute, hence same

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)
#print(w1.getX()) # error as x and y within the function aren't defined


