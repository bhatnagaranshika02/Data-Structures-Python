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


v=Vertex(1)
v.add_n(2)
print(v.getconnections())
print(v.getId())
print(v.getWeight(2))
