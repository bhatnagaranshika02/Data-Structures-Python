def insert(self,data):
    if self.root is None:
        root=Node(data)
        root.color='black'
        
    else:
        current=self.root
        
        while True:
            if data<current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=Node(data)
                    
        
