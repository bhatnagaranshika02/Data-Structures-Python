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
				self.chessTable[rowindex][colIndex]=1

				if self.solve(colIndex+1):
					return True
				
				self.chessTable[rowindex][colIndex]=0

	
	def isPlaceValid(self,rowindex,colIndex):
		for i in range(colIndex):
			if self.chessTable[rowindex][i] == 1:
				return False
		j = colIndex
		for i in range(rowindex,-1,-1):
			if j<0:
				break
			if self.chessTable[i][j] == 1:
				return False
			j =j-1
		j = colIndex
		for i in range(rowindex,len(self.chessTable)):
			if j<0:
				break
			if self.chessTable[i][j]:
				return False

			j= j-1
		return True

	def printQueens(self):
		for i in range(self.numOfQueens):
			for j in range(self.numOfQueens):
				if self.chessTable[i][j] ==1:
					print( ' * ',end ="")
				else:
					print(' - ',end="")
			print('\n')


if __name__ == "__main__":
	obj = QueensProblem(100)
	obj.solveQueensProblem()
