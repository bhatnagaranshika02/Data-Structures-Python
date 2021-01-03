class tree:
    def __init__ (self,val):
        self.data = val
        self.right = None
        self.left = None

    def search_node(self,root,key):
        if root is None:
            return False
        if root.data == val:
            return True
        res1 = self.search(root.left,key)
        if res1:
            return True
        res2 = self.search(root.right,key)
        return res2
