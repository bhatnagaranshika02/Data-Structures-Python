def Graph:
	def __init__ (self,virtex):
		self.v = vertex
		self.graph = defaultdict(list)

	def addEdge(self,v,w):
		self.graph[v].append(w)
		self.graph[w].append(v)


    def isCycle(self,v,visited,parent):
    	visited[v]=True

    	for i in self.graph[v]:
    		if visited[i] == False:
    			if (self.isCycle(i,visited,v)) == True:
    				return True
            elif i!=parent:
            	return True
        return False

    def isTree(self,v):
    	visited = [False]*self.v
    	if (isCycle(0,visited,-1)) == True:
    		return False

    	for i in range(self.v):
    		if visited[i] == False:
    			return False
    	return True




