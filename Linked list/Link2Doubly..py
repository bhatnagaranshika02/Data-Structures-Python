class Node:
    def __init__(self,data,prev=0,next=0):
        self.data=data
        self.prev=prev
        self.next=next

class linked_list:
    def __init__ (self):
        self.start=None
        

    def addfront(self,data):
        new_node=Node(data)
        new_node.prev=None
        new_node.next=self.start
        if self.start is not None:
            self.start.prev=new_node
        else:
            self.start=new_node
            
    def deletefront(self,data):
        if self.start==None:
            print("List is empty")
        else:
            self.start=self.start.next

    def delete(self,node):
        temp=self.start
        while temp:
            if temp.data==node.data:
                prevs=temp.prev
                temp.next.prev=prevs
                prevs.next=temp.next
                break
            else:
                temp=temp.next
                



    def removedupli(self):
        temp=self.start
        l=[]
        while temp:
            if temp.data not in l:
                l.append(temp.data)
                temp=temp.next
            else:
                nxt=temp.next
                self.delete(temp)
                temp=nxt
            

           
        
    def addbefore(self,data,beforewhat):
        new_node=Node(data)
        if self.start==None:
            print("List is empty")
        else:
            
            temp=self.start
            before=temp
            
            while temp!=None:
                if temp.data!=beforewhat:
                   before=temp
                   temp=temp.next
                else:
                   before.next=new_node
                   new_node.next=temp
                   break
                
                
    def deletebefore(self,beforewhat):
        if self.start==None or self.start==beforewhat:
            print("Cant delete")
        else:
            temp=self.start
            while temp!=None:
                if temp.data==beforewhat:
                    if temp.prev==self.start:
                        self.start=temp
                    else:
                        
                        prevs=temp.prev.prev
                        temp.prev=prevs
                    
                        break
                else:
                    temp=temp.next
                
                
            
    def addafter(self,data,addafter):
        new_node=Node(data)
        temp=self.start
        while temp!=None:
            if temp.data==addafter:
                temp2=temp.next
                temp.next=new_node
                new_node.next=temp2
                new_node.prev=temp
               
                break
            else:
                temp=temp.next

    def deleteafter(self,afterwhat):
        if self.start==None or self.start==afterwhat:
            print("Cant delete")
        else:
            temp=self.start
            while temp.next!=None:
                if temp.data==afterwhat:
                    nexts=temp.next.next
                    temp.next=nexts
                    
                    break
                else:
                   temp=temp.next
                    
                
       
            


    def addlast(self,data):
        new_node=Node(data)
        temp=self.start
        while temp!=None:
            if temp.next==None:
                temp.next=new_node
                new_node.prev=temp
                new_node.next=None
                break
            else:
                temp=temp.next
                
               
            
            
    def traverse(self):
        if self.start==None:
            print("List is empty")
        else:
            
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
            print("\n")

    def count(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            count=0
            while temp!=None:
               count+=1
               temp=temp.next
            print("Total count is:",count)


            

obj=linked_list()
obj.count()
obj.addfront(6)
obj.addafter(7,6)
obj.addafter(8,7)
obj.addafter(9,8)
obj.traverse()
obj.addbefore(88,8)
obj.traverse()
obj.deleteafter(88)
obj.traverse()
obj.deletebefore(7)
obj.traverse()
obj.deleteafter(7)
obj.traverse()
obj.deletebefore(9)
obj.traverse()
obj.addafter(10,9)
obj.addafter(11,10)
obj.addafter(11,11)
obj.traverse()
obj.removedupli()
obj.traverse()


