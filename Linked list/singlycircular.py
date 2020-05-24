class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularSingly:
    def __init__(self):
        self.last=None

    def addtoempty(self,data):
        new_node=Node(data)
        self.last=new_node
        self.last.next=self.last

        
    def addstart(self,data):
        new_node=Node(data)
        new_node.next=self.last.next
        self.last.next=new_node

    def addend(self,data):
        new_node=Node(data)
        if self.last==None:
            print("list is empty")
        else:
            new_node.next=self.last.next
            self.last.next=


    def traverse(self):
        if self.last==None:
            print("List is empty")
        else:
            temp=self.last.next
            while temp:
                print(temp.data,end=' ')
                temp=temp.next
                if temp==self.last.next:
                    break
            print('\n')

c=circularSingly()
c.addlast(6)
c.addstart(1)
c.traverse()
c.addstart(2)
c.traverse()
c.addlast(7)
c.traverse()
