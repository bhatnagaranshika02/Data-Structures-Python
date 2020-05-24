class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class Binary_tree(object):
    def __init__(self,root):
        self.root=Node(root)

n=Binary_tree(1)
n.root.left=Node(2)
n.root.right=Node(3)
n.root.left.left=Node(4)
