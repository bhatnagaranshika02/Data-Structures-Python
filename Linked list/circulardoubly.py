class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class Circular:
    def __init__(self):
        self.start=None
        
    def add(self,data):
        new_node=Node(data)
        self.start=new_node
        new_node.prev=new_node
    def addafter(self,data,afterwhat):
         new_node=Node(data)
         if self.start==None:
             print("List is empty")
         else:
             temp=self.start
             while temp!=None:
                 if temp.data==afterwhat:
                     temp2=temp.prev
                     temp3=temp2.prev
                     temp.prev=temp3
                     break
                 else:
                    temp=temp.next

    def addafter(self,data,afterwhat):
           new_node=Node(data)
           if self.start==None:
               print("List is empty")
           else:
               temp=self.start
               while temp!=None:
                   if temp.data==afterwhat:
                       temp2=temp.next
                       temp3=temp2.next
                       temp.next=temp3
                       break
                   else:
                       temp=temp.next
    def traverse(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data)
                temp=temp.next
            print("\n")



                    
c=Circular()
c.add(3)
c.addafter(4,3)
c.addbfore(2,3)
c.traverse()
                       
                       
        
             
        
        
