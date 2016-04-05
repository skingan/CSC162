# sarah kingan
# CSC162, summer2015
# Lab 16
#
# Using breadth first search write an algorithm that can 
# determine the shortest path from each vertex to every 
# other vertex. This is called the all pairs shortest path 
# problem.
#
# some code modified from Problem Solving with Algorithms 
# and Data Structures, By Brad Miller and David Ranum
#
# http://www.codeskulptor.org/#user40_x9mT4tViDU_5.py
#
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id)
#        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return (x for x in self.vertList.values())

    
def FloydWarshall(graph):
    M = weightMatrix(graph)
    V = len(M[0])
    for k in range(V):
        for i in range (V):
            for j in range (V):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]
    return M


def weightMatrix(graph):
# initialize matrix with infinity edges
    V = len(graph.getVertices())
    M = [[float("inf") for i in range(V)] for j in range(V)]
# add 0 for self-self
    for i in range(V):
        for j in range(V):
            if i == j:
                M[i][j] = 0
# import weights from graph object
    for v in graph:
        for adj in v.getConnections():
            M[int(v.getId())][int(adj.getId())] = v.getWeight(adj)
    return M


# make graph
g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,5,3)
g.addEdge(3,4,7)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

# compute minimum pairwise distances with Floyd Warshall algorith
dist = FloydWarshall(g)
# print distance matrix
for i in range(len(dist[0])):
    print dist[i]
        
        
        
        
        
        