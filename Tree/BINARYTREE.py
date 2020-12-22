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
def levelorder(root):
    if root is None:
        print("Empty tree")
    else:
        q=[]
        q.append(root)
        while q:
            root=q[0]
            print(q.pop(0).key,end='\n')
            if root.left:
                q.append(root.left)
            
            if root.right:
                q.append(root.right)

def size(root):
    if root is None:
        return "empty"
    else:
        count=1
        q=[]
        q.append(root)
        while q:
            root=q[0]
            q.pop(0)
            if root.left:
                count+=1
                q.append(root.left)
            if root.right:
                count+=1
                q.append(root.right)
        return count
    
def MergeBinaryTree(t1,t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.val += t2.val
    t1.left = MergeBinaryTree(t1.left,t2.left)
    t1.right = MergeBinaryTree(t1.right,t2.right)
    return t1

def findDepth(root):
    if root is None:
        return 0
    ans=0
    l=findDepth(root.left)
    r=findDepth(root.right)
    if abs(l-r)>1:
        ans=0
    return max(l,r)+1
        

def isBalanced(A):
    ans= findDepth(A)
    return ans

        
if __name__ == '__main__':
    root = newNode(10) 
    root.left = newNode(11) 
    root.left.left = newNode(7) 
    root.right = newNode(9) 
    root.right.left = newNode(15) 
    root.right.right = newNode(8)
    levelorder(root)
    print('\n','size is: ',size(root))
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root) 
 
    key = 12
    insert(root, key) 
    print() 
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)
    print('\n','new size is: ',size(root))
    print(isBalanced(root))
 
