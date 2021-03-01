class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head1=None
        self.head2=None

    def add1(self,data):
        newnode=Node(data)
        if self.head1 is None:
            self.head1=newnode
            newnode.next=None
        else:
            temp=self.head1
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            newnode.next=None

    def add2(self,data):
        newnode=Node(data)
        if self.head2 is None:
            self.head2=newnode
            newnode.next=None
        else:
            temp=self.head2
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            newnode.next=None
    def merge(self):
        temp=self.head1
        while temp.next !=None:
            temp.next = temp
        temp.next=self.head2

    def sort(self):
        curr=self.head1
        temp=self.head1
        while curr.next!=None:
            temp.curr.next
            while(temp!=None):
                if temp.data<curr.data:
                    temp.data,curr.data=curr.data,temp.data
                temp=temp.next
            curr=curr.next
            





























            
        
                
            
