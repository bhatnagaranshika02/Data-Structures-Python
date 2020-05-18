class Node(object):
    sef __init__ (self,data):
        self.data=data
        self.right=None
        self.left=None

class BST(object):
    def __init__ (self,root):
        self.root=Node(root)

    def insert(self,new_val):
        self.insert_helper(self.root,new_val)

    def insert_helper(self,current,new_val):
        if current.data<new_val:
            if current.right:
                
