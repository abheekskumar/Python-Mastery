

# Adjacency Matrix:
graph1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

#OR
graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
# Each key is a node, their value is a list of nodes that they're connected to

# OOP representation:
class Graph:
    def __init__(self):
        self.adj = {}
    def addNode(self,node):
        if node not in self.adj:
            self.adj[node] = []
    def addEdge(self,u,v):
        self.addNode(u)
        self.addNode(v)
        self.adj[u].append(v)
        self.adj[v].append(u) # remove this for directed graphs

    def neighbours(self,node):
        return self.adj.get(node,[])
    
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3,8)
g.addEdge(3,6)
g.addEdge(2,7)
g.addEdge(1,7)
print(g.adj)  

# BFS
from collections import deque

def bfs(graph,start):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        print(node)
        visited.add(node)
        for neighbour in graph.adj[node]:

            if neighbour not in visited:
                queue.append(neighbour)
print("BFS:")
bfs(g,0)

def dfs(graph,start,visited = None):
    if visited is None:
        visited = set()
    if start in visited:
        return
    
    print(start)
    visited.add(start)
    for neighbour in graph.adj[start]:
        dfs(graph,neighbour,visited)

print("DFS:")
dfs(g,0)