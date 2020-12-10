from collections import defaultdict
class Graph:
	def __init__ (self,vertices):
		elf.v = vertices
		self.graph = defaultdict(list)

	def addEdge(self,v,w):
		self.graph[v].append(w)
		self.graph[w].append(v)

	def isCycle(self,v,visited,parent):
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] is False:
				if self.isCycle(i,visited,v):
					return True
		    elif parent!=i:
		    	return True
		return False

	def isCyclic(self):
		visited = [False]*(self.v)
		for i in range(self.v):
			if visited[i] == False:
				if (self.isCycle(i,visited,-1))==True:
					return True
		    return False


g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
if g.isCyclic(): 
    print "Graph contains cycle"
else : 
    print "Graph does not contain cycle "
g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
  
  
if g1.isCyclic(): 
    print "Graph contains cycle"
else : 
    print "Graph does not contain cycle "
