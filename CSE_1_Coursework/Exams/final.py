def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception. 
    """
    res = 0
    digit = True
    for char in s:
        if char.isdigit():
            res +=1
        else:
            digit = False
    
    if digit == False:
        raise ValueError()
    return res
# sum_digits("3234")

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    numsFreq = {}
    for ele in L:
        numsFreq[ele] = numsFreq.get(ele,0) + 1
    most = None
    for k,v in numsFreq.items():
        if v%2 != 0:
            if k > most or most is None:
                most = k
    return most
    
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    if len(aDict) == 0: # base case
        return []
    
    res = []
    lVals = aDict.values()
    for k,v in aDict.items():
        if lVals.count(v) > 1:
            continue # move to next element
        else:
            res.append(k)
    return res.sorted()

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    count = {}
    for v in aDict.values():
        count[v] = count.get(v,0) +1
    
    unique = [v for v,c in count.items() if c == 1]
    keysWithUnique = [k for k,v in aDict.items() if v in unique]
    return sorted(keysWithUnique)



### Problem 6:
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return Person.say(self," It is obvious that " + Person.say(self,stuff))
    def lecture(self,stuff):
        return "It is obvious that" + Person.say(self,stuff)



### Problem 7:
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)

class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        Campus.__init__(self,center_loc)
        self.tent_loc = []
        self.tent_loc.append(tent_loc)
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        for tent in self.tent_loc:
            if tent.dist_from(new_tent_loc) >= 0.5:
                pass
            else:
                return False
        self.tent_loc.append(new_tent_loc)
        return True
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        for tent in self.tent_loc:
            if  tent== tent_loc:
                self.tent_loc.remove(tent)
                return None
        raise ValueError("Tent not found.")
        
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
    
        # merge sorting:
        def merge(L1,L2):
            res = []
            idx1 = idx2 = 0
            while idx1 < len(L1) and idx2 < len(L2): # till one of them runs out
                if L1[idx1].getX() < L2[idx2].getX(): # where ever a comparison takes place, that's where we should change
                    res.append(L1[idx1])
                    idx1 +=1
                else:
                    res.append(L2[idx2])
                    idx2 +=1
            # for adding the rest of the elements:
            while len(L1) > idx1:
                res.append(L1[idx1])
                idx1 +=1
            while len(L2) > idx2:
                res.append(L2[idx2])
                idx2 +=1
            return res
        
        def mergeSort(L):
            # base case: recur all the way down to 2 elements
            if len(L) == 1 or len(L) == 0: #
                return L[:] # this should be a copy
            # cause we might be modifying on the go
            else:
            # recursive case:
                half = len(L)//2
                left = mergeSort(L[:half])
                right = mergeSort(L[half:])
                return merge(left,right)

        return [str(tentLoc) for tentLoc in mergeSort(self.tent_loc)]


        