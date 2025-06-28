# learning OOP in python

# __init__ - used to construct an instance of that class
class Rect:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

x = Rect(12,54)
print(x.length)
print(x.breadth)

def main():
    pass


if __name__ == "__main__":
    main()