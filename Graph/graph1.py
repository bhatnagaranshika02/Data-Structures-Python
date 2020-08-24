class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedto={}

    def add_n(self,nbr,weight=0):
        self.connectedto[nbr] = weight

    def getconnections(self):
        return self.connectedto.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedto[nbr]
class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
        
    def addVertex(self,key):
        self.numVertices+=1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].add_n(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

v=Vertex(1)
v.add_n(2)
print(v.getconnections())
print(v.getId())
print(v.getWeight(2))
