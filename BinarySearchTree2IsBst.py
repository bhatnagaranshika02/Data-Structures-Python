class Node(object):
    def __init__ (self,data):
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
                return self.insert_helper(current.right,new_val)
            else:
                current.right=Node(new_val)

        else:
            if current.left:
                return self.insert_helper(current.left,new_val)
            else:
                current.left=Node(new_val)
        



    def is_bst(self):
        def helper(node,lower=float('-inf'),upper=float('inf')):
            if not node:
                return True
            val=node.data
            if val<=lower or val>=upper:
                return False
            if not helper(node.left,lower,val):
                return False
            if not helper(node.right,val,upper):
                return False
            return True
        return helper(self.root)



bst = BST(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(bst.is_bst())
print(tree.is_bst())

    













