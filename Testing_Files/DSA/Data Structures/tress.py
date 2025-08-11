from typing import List



class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = [] # empty list

    def addChild(self,child_node):
        self.children.append(child_node)


class Trees:
    def __init__(self,data):
        self.root = TreeNode(data)

    # insertion



    # deletion
    def removeNode(self,data):
        pass


    # searching



    # traversal
    def printTree(self,node, level = 0):
        if node:
            print(" "*level + str(node.data))
            for child in node.children:
                self.printTree(child, level+1)



# Binary Trees

class TreeNode:
    def __init__(self,data = 0,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right


# trees as lists in level order traversal:
L1 = [1, 2, 3, None, 4]

# converting this list into a tree:
from collections import deque

def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root
 

 # sample DFS Traversal:
 # Inorder: left -> root -> right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Preorder: root -> left -> right
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# Postorder: left -> right -> root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


# sample BFS:
from collections import deque

def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
