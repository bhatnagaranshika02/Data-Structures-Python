class Node:
    def __init__ (self,node):
        self.node=node
        self.left=None
        self.right=None

class binary:
    def __init__ (self):
        self.root=None
    def create(self,data):
        if self.root==None:
            root=Node(data)
        else:
            current=self.root
            while True:
                if data<cuurent.node:
                    if current.left:
                        current=current.left
                    else:
                        current.left=Node(data)
                        break
                elif data>current.node:
                    if current.right:
                        current=current.right
                    else:
                        current.right=Node(data)
                        break
                else:
                    break

    

def post_order(root):
    if root is None:
        return False
    else:
        if root.left():
            return left.post_order()
        if root.right:
            return right.post_order()
        print(node)


def MirrorImage(root):
    if root is not None:
        MirrorImage(root.left)
        MirrorImage(root.right)
        temp=root.left
        root.left=root.right
        root.right=temp


obj=binary()
l=list(map(int,input().split()))
for i in l:
    obj.create(i)
print(post_order(obj.root))
print(MirrorImage(obj.root))
