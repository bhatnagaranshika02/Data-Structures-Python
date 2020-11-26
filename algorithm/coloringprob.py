class ColoringProblem:

	def __init__ (self,numOfVert,numofcolors,graph):
		self.numOfVert = numOfVert
		self.numofcolors = numofcolors
		self.colors = [0]*numOfVert
		self.graph = graph


	def solveColoringProblem(self):
		if not self.solve(0):
			self.showResult()
		else:
			print("No feasible solution.")


	def solve(self,nodeIndex):
		if nodeIndex == self.numOfVert:
			return True

		for color in range(1,self.numofcolors+1):
			if self.isColorValid(nodeIndex,colorIndex):
				self.colors[nodeIndex] = colorIndex

				if self.solve(nodeIndex+1):
					return True 
				#backtrack 
		return False
    

    def isColorValid(self,nodeIndex,colorIndex):
    	for i in range(self.numOfVert):
    		if self.graph[nodeIndex][i] == 1 and colorIndex == self.colors[i]:
    			return False
    	return True


    def showResult(self):
    	for i in range(self.numOfVert):
    		print("Node %d has color index %d",%(i,self.colors[i]))


numOfVert = int(input("Enter the number of vertices: "))
numofcolors = int(input("Enter the number of colors: "))
graph = []
for i in range(numOfVert):
	vert.append(list(map(int,input().split(" "))))
	graph.append(vert)

obj = ColoringProblem(numOfVert.numofcolors,graph)
obj.solveColoringProblem()










