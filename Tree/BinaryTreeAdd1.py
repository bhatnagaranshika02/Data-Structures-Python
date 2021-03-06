class newNode():
    def __init__ (self,data):
        self.key = data
        self.left = None
        self.right = None

def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.key,end= " ")
    inorder(temp.right)

def insert(root,key):
    if root is None:
        root = newNode(key)
    else:
        q=[]
        q.append(root)
        while q:
            root=q[0]
            q.pop(0)

            if not root.left:
                root.left = newNode(key)
                break
            else:
                q.append(root.left)

            if not root.right:
                root.right = newNode(key)
                break
            else:
                q.append(root.right)

        
if __name__ == '__main__':
    root = newNode(10) 
    root.left = newNode(11) 
    root.left.left = newNode(7) 
    root.right = newNode(9) 
    root.right.left = newNode(15) 
    root.right.right = newNode(8) 
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root) 
 
    key = 12
    insert(root, key) 
    print() 
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)
 
