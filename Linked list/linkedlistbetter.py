class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.next=None

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
        print('\n')

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_after(self,data,after_what):
        new_node=Node(data)
        temp=self.head
        while temp:
            if temp.data==after_what:
                after=temp.next
                temp.next=new_node
                new_node.next=after
                break
            else:
                temp=temp.next
        else:
            print("Node doesn't exist")

    def delete_byvalue(self,key):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.start
            while temp and temp!=key:
                prev=temp
                temp=temp.next
            if temp is None:
                return
            else:
                prev.next=temp.next
                temp=None

    '''   def delete_byposition(self,value)
        if self.head:
            temp=self.head
            if value==0:
                self.head=temp.next
                temp=None
                return
            prev=None
            count=0
                '''

                
 
    def count(self,node):
         if node is None:
             return 0
         else:
            return 1+self.count(node.next)
                
            

mylist=Linked_list()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)
mylist.insert_after(55,5)
mylist.print_list()
print(mylist.count(mylist.head))
