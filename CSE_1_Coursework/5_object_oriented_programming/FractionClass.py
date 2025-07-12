

class Fractions(object):
    """Creates a number representation of a float as numerator/denominator"""

    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return (str(self.numerator)+"/"+str(self.denominator))
    
    def eval(self):
        return self.numerator/self.denominator
    def getNumerator(self):
        return self.numerator
    def getDenominator(self):
        return self.denominator
    
    def __eq__(self,other):
        return (self.eval() == other.eval()) 
    
    def __add__(self,other):
        numerator = self.numerator*other.denominator + other.numerator*self.denominator
        denominator = self.denominator * other.denominator
        return Fractions(numerator,denominator)
    def __sub__(self,other):
        numerator = self.numerator*other.denominator - other.numerator*self.denominator
        denominator = self.denominator * other.denominator
        return Fractions(numerator,denominator)
    def __mul__(self,other):
        numerator = self.numerator*other.numerator
        denominator = self.denominator * other.denominator
        return Fractions(numerator,denominator)
    def __truediv__(self,other):
        numerator = self.numerator*other.denominator
        denominator = self.denominator * other.numerator
        return Fractions(numerator,denominator)
    

half = Fractions(1,2)
quarter = Fractions(1,4)
three_forths = Fractions(3,4)
result1 = Fractions.__add__(half,quarter)


print(result1)
print(result1 == three_forths)
print(Fractions.eval(half * quarter)) # half*quarter returns 
print(Fractions.eval(half / quarter))
