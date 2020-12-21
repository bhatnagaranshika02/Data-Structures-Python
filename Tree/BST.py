class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def deleteNode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left = deleteNode(root.left,key)
    elif(key>root.key):
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.left
            root=None
            return temp






r=Node(50)
r = insert(r, 30) 
r = insert(r, 20) 
r = insert(r, 40) 
r = insert(r, 70) 
r = insert(r, 60) 
r = insert(r, 80)

inorder(r)
    
