class Node:
    def __init__(self,next=None,prev=None,data=None):
        self.next=next
        self.prev=prev
        self.data=data

class doublyLinked:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node =Node(data=new_data)
        new_node =self.head
        new_node.prev=None
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node

    def print(self,node):
        print("Lets traverse")
        while node is not None:
            print(node.data)

obj = doublyLinked()
obj.push(5)
obj.push(8)
obj.push(9)
obj.push(10)
