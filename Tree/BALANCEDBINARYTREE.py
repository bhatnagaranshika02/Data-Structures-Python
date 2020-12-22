def findDepth(self,root):
    if root is None:
        return 0
    l=self.findDepth(A.left)
    r=self.findDepth(A.right)
    if abs(l-r)>1:
        self.ans=0
    return max(l,r)+1
        

def isBalanced(self,A):
    self.findDepth(A,0)
    return self.ans
        
