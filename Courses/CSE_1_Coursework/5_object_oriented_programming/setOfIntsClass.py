

class setOfInts:
    """ Creates a setOfInts type"""
    def __init__(self) -> None:
        self.vals = list()

    def __str__(self) -> None:
        if len(self.vals) == 0:
            return "{}"
        
        result = "{"
        for ele in self.vals:
            if ele == self.vals[-1]:
                result += str(ele)
            else:
                result += str(ele)
                result += ","
        result += "}"
        return result
    
    def __len__(self) -> int:
        return len(self.vals)
    
    def insert(self,e) -> None:
        """ Adds e to set. If present, raises value error"""
        if e in self.vals:
            raise ValueError(f"{e} is already in {self}.")
        self.vals.append(e) 

    def member(self,e) -> bool:
        """ Returns Boolean based on wheter or not e is in set."""
        if e in self.vals:
            return True
        return False
    
    def remove(self,e) -> None:
        """ Removes e if present in set. Else, raises value error."""
        if e in self.vals:
            self.vals.remove(e)
            return None # return just to stop flow of control
        raise ValueError(f"{e} not Found")

def printx():
    global x
    print(x,len(x))

x = setOfInts()
printx()
x.insert(23)
x.insert(26)
printx()
print(x.member(23))
x.remove(23)
printx()
x.remove(23)
printx()


        
        