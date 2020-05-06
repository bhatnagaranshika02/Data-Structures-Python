class Node:
    def __init__(self,d,n=None):
        self.data = d
        self.next_node=n


    def get_next(self):
        return self.next_node

    def set_next(self,n):
        self.data = n

    def get_data(self):
        return self.data

    def set_data(self,d):
        self.data=d

class Linked_list(object):
    def __init__(self,r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size+=1
        
    def remove(self):
        pass

    def find(self):
        pass


myList = Linked_list()
myList.add(5)
print("Initial size is:",myList.get_size())
myList.add(6)
myList.add(7)
myList.add(8)
myList.add(9)
print("Final Size is: ",myList.get_size())
    
        
        
