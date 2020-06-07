
class ABC:

    def Iterative(self,numList):
        thesum=0
        for i in numList:
            thesum+=i
        return thesum

    def Recursive(self,numList):
        if len(numList) == 1:
            return numList[0]
        else:
            return numList[0]+self.Recursive(numList[1:])

a=ABC()
print(a.Iterative([1,3,5,7,9]))
print(a.Recursive([1,3,5,7,9]))
        
