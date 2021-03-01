class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            newnode.next=None
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
        newnode.next=None

    def middle(self):
        fast=self.head
        slow=self.head
        if self.head==None:
            return None
        while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next

        return slow.data

n=list(map(int,input().split()))
obj=linkedlist()
for i in n:
    obj.insert(i)

print('\n',obj.middle())
