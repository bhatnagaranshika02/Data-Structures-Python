class HamiltonianProblem:
	def __init__ (self,adjacencyMatrix):
		self.numofVert = len(adjacencyMatrix)
		self.hamiltonianPath = [None]*self.numofVert
		self.adjacencyMatrix = adjacencyMatrix

	def hamiltonianCycle(self):
		self.hamiltonianPath[0] = 0
		if not self.findFeasibleSolution(1):
			print("No Feasible Solution found.")
		else:
			self.showHamiltonianPath()

	def findFeasibleSolution(self,position):
		if position == self.numofVert:
			x = self.hamiltonianPath[position -1]
			y = self.hamiltonianPath[0]

			if self.adjacencyMatrix[x][y] == 1:
				return True
			else:
				return False

		for vertex in range(1,self.numofVert):
			if self.isFeasible(vertex,position):
				self.hamiltonianPath[position] = vertex

				if self.findFeasibleSolution(position+1):
					return True
		return False


	def isFeasible(self,vertex,actualposition):
		if self.adjacencyMatrix[self.hamiltonianPath[actualposition-1]][vertex]==0:
			return False


		for i in range(actualposition):
			if self.hamiltonianPath[i] == vertex:
				return False
		return True

	def showHamiltonianPath(self):
		print("Hamiltonian Cycle does exist..!!\n")
		for i in range(self.numofVert):
			print(self.hamiltonianPath[i])

		print(self.hamiltonianPath[0])

l=[]
n = int(input())
adjacencyMatrix = []
for i in range(n):
	l.append(list(map(int,input().split(' '))))
	adjacencyMatrix.append(l)
hamiltonian = HamiltonianProblem(adjacencyMatrix)
hamiltonian.hamiltonianCycle()

