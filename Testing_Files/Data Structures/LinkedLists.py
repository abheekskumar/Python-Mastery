# Linked Lists Implementation:


# Node implementation

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None # pointer to the next node

# Linked Lists Implementation
class LinkedList:
    def __init__(self):
        self.head: Node= None # first node
        self.tail: Node= None # last node
        self.length = 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        if self.length == 0:
            return "List is empty"
        current_node = self.head
        res = ""
        while current_node != None:
            res += str(current_node.data)
            res += "->"
            current_node = current_node.next
        res += "END"
        return res
    
    
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def prepend(self,data):
        new_node = Node(data)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self,data, index):
        if index == 0:
            self.prepend(data)
            return
        
        current_node = self.head
        position = 0

        while ((current_node != None) and (position+1 != index)):
            current_node = current_node.next
            position +=1
        
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
            if new_node.next is None:
                self.tail = new_node
        else:
            print("Index not present")

    def update_node(self,data,index):

        current_node = self.head
        position = 0

        while ((current_node != None) and (position+1 != index)):
            current_node = current_node.next
            position +=1

        if (current_node != None):
            current_node.data = data
        else:
            print("Index not present")

    def remove_node(self,data):
        if self.length == 0:
            print("Linked list is empty.")
            return
        
        current_node = self.head
        previous_node = None
        while ((current_node != None)):
            if current_node.data == data:
                previous_node.next = current_node.next
                del current_node
                return
            previous_node = current_node
            current_node = current_node.next
        print(f"{data} wasn't present in the Linked List.")

    def get(self,index):
        if self.length == 0:
            print("Linked List is empty.")
            return

        current_node = self.head
        position = 1

        while ((current_node!= None) and (position != index)):
            current_node = current_node.next
            position += 1

        if current_node != None:
            print(current_node.data)
        else:
            print("Index out of bounds.")
        


LL = LinkedList()



LL.size()
LL.printList()
LL.append(23)
LL.append("Hello World")
LL.printList()
LL.prepend(1)
LL.printList()

LL.get(1)
LL.get(2)
LL.get(3)


LL.insert(65,2)
LL.printList()

LL.remove_node(523)
LL.remove_node(65)
LL.printList()

