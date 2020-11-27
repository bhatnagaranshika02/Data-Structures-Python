class QueensProblem:
	def __init__ (self,numOfQueens):
		self.numOfQueens = numOfQueens
		self.chessTable  = [[None for i in range(numOfQueens)] for j in range(numOfQueens)]

	def solveQueensProblem(self):
		if self.solve(0):
			self.printQueens()
		else:
			print("There is no solution..")

	def solve(self,colIndex):
		if colIndex == self.numOfQueens:
			return True
		for rowindex in range(self.numOfQueens):
			if self.isPlaceValid(rowindex,colIndex):
				self.chessTable[rowindex] = colIndex

				if self.solve(colIndex+1):
					return True
				
				self.chessTable[rowindex][colIndex] =0


