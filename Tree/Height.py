class Node:
    def __init__ (self,node):
        self.node=node
        self.left=None
        self.right=None

class binary:
    def __init__ (self):
        self.root=None

    def create(self,val):
        if self.root==None:
            self.root=Node(val)
        else:
            current=self.root
            while True:
                if val<current.node:
                    if current.left:
                        current=current.left
                    else:
                        current.left=Node(val)
                        break
                elif val > current.node:
                    if current.right:
                        current=current.right
                    else:
                        current=Node(val)
                        break
                else:
                    break

def height(root):
        if root==None:
            return -1
        else:
            left=height(root.left)
            right=height(root.right)
            
            return 1+ max(left,right)



tree = binary()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

p=
height(tree.root)
print(p)
