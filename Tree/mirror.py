class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None


def mirror(node):
    if (node == None):
        return
    else:
        temp = node
        mirror(node.left)
        mirror(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp
        
