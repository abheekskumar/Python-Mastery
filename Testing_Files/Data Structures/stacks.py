# OOP Approach:
class Stack:
    def __init__(self):
        """ Initializes an empty stack based on LIFO principle."""
        self.stack = []
    def __str__(self):
        res = ""
        for ele in self.stack[::-1]:
            res += str(ele)
            res += "\n"
        return res

    def push(self,element) -> None:
        """ Pushes element onto the top of the stack"""
        self.stack.append(element)

    def pop(self) -> int:
        """ Removes and returns the element on the top of the stack."""
        try:
            return self.stack.pop()
        except Exception:
            return "Stack is empty."
        
    def peak(self) -> int: #AKA TOP
        """Returns the topmost element of the stack."""
        try:
            return self.stack[-1]
        except:
            return "Stack is empty."
        
    def isEmpty(self) -> bool:
        return len(self.stack) == 0
    
    def size(self) -> int:
        return len(self.stack)

s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
print(s1)
s1.pop()
print(s1)

# Functional approach:

def pushStack(stack:list,element)-> None:
    """Pushes element onto the top of the stack"""
    stack.append(element)

def peakStack(stack:list):
    """Returns topmost element of the stack. If empty, returns a distinct statement."""
    try:
        return stack[-1]
    except Exception:
        return "Stack is empty."
    
def popStack(stack:list):
    """ Removes and returns the topmost element of the stack. If empty, returns a distinct statement."""
    try:
        return stack.pop()
    except Exception:
        return "Unable to pop as stack is empty."

s2 = []
pushStack(s2,1)
pushStack(s2,2)
pushStack(s2,3)
pushStack(s2,4)
pushStack(s2,5)
print(s2)
popStack(s2)
print(s2)

# using collections
from collections import deque
# deque is double ended que, safer and faster approach.
stack1 = deque()
stack1.append() # push
stack1.pop() # pop

# or use this function implemented in OOP
    