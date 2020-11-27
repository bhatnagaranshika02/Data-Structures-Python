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

	def isValid(self,x,y):
		if x<0 or x >= self.mazeSize:
			return False
		if y<0 or y>=self.mazeSize:
			return False
		if self.mazeTable[x][y] == 0:
			return False

		return True

	def showResult(self):
		for i in range(self.mazeSize):
			for j in range(self.mazeSize):
				if self.solutionTable[i][j] == 1:
					print(' S ',end = "")
				else:
					print(' - ',end = "")

			print('\n')

if __name__ == "__main__":
	mazeTable = [[1,1,1,1,1],
	             [1,0,0,1,0],
	             [0,0,0,1,0],
	             [1,1,1,1,1],
	             [1,1,1,0,1]]

	MazeProblem = MazeProblem(mazeTable)
	MazeProblem.solveMaze()



















