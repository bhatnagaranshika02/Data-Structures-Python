class newnode:

    def __init__ (self,data):
        self.key = data
        self.left = None
        self.right = None

    def printInorder(Node):
        if Node is None:
            return
        printInorder(node.left)
        print(node.data,end=" ")
        printInorder(node.right)

inorder=[4,8,10,12,14,20,22]
