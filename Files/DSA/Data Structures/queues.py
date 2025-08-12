# OOP approach:

class Queue():
    def __init__(self):
        """Initializes an empty queue based on FIFO principle."""
        self.queue = []
    def __str__(self):
        return str(self.queue)
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue(self):
        try:
            return self.queue.pop(0)
        except Exception:
            return "Queue is empty."
    def front(self):
        try:
            return self.queue[0]
        except Exception:
            return "Queue is empty"
        

q1 = Queue()
q1.enqueue(23)
q1.enqueue(65)
q1.enqueue(87)
q1.enqueue(54)
print(q1.dequeue())
print("*")
print(q1)

# Functional approach:

def queueEnqueue(queue: list,element)->None:
    """ Enqueues element onto the back of the queue."""
    queue.append(element)
def queueDequeue(queue:list):
    """ Dequeues frontmost element of the queue."""
    try:
        return queue.pop(0)
    except Exception:
        return "Queue is empty"
def queueFront(queue:list):
    """ Returns the first element in the queue."""
    try:
        return queue[0]
    except Exception:
        return "Queue is empty"
    
q2 = []
queueEnqueue(q2,23)
queueEnqueue(q2,65)
queueEnqueue(q2,87)
queueEnqueue(q2,54)
print("Functional Approach:")
print(queueDequeue(q2))
print("*")
print(q2)


# using collections module
from collections import deque
q3 = deque()
q3.append() # enque
q3.popleft() # deque
q3[0] # front