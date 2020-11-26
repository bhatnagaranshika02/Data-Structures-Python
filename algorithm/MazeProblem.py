class MazeProblem:
	def __init__ (self,mazeTable):
		self.mazeTable = mazeTable
		self.mazeSize = len(self.mazeTable)
		self.solutionTable = [[0]*self.mazeSize for x in range(self.mazeSize)]
	def solveMaze(self):
		if self.solve(0,0):
			self.showResult()
		else:
			print("No feasible solution")

	def solve(self,x,y):
		if self.isFinished(x,y):
			return True
		if self.isValid(x,y):
			self.solutionTable[x][y] = 1
			if self.solve(x+1,y):
				return True
			if self.solve(x,y+1):
				return True

	def isFinished(self,x,y):
		if x == self.mazeSize-1 and y ==self.mazeSize-1:
			self.solutionTable[x][y] =1
			return True
		return False