class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__ (self):
        self.start=None
    def insert(self,value):
        new_node = Node(value)
        if self.start==None:
            self.start=new_node
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node


    def deletefirst(self):
        if self.start==None:
            print("List is empty")
        else:
            self.start=self.start.next

             
    def traverse(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
            print('\n')

    def countnode(self):
        if self.start==None:
            print("List has 0 nodes")
        else:
            temp=self.start
            count=1
            while temp.next!=None:
                count+=1
                temp=temp.next
            print("Total number of nodes are: ",count)77

            
    def addafter(self,afterwhat,data):
        new_node=Node(data)
        if self.start==None:
            self.start=new_node
        else:
            temp=self.start
            while temp.next!=None:
                if temp.data==afterwhat:
                    temp2=temp.next
                    temp.next=new_node
                    new_node.next=temp2
                    break
                else:
                    temp=temp.next
                    

    def deleteafter(self,data):
       if self.start==None:
           print("List is empty")
       else:
            temp=self.start
            while temp!=None:
                if temp.data==data:
                    temp2=temp.next
                    temp3=temp2.next
                    temp.next=temp3
                    break
                else:
                    temp=temp.next
            

                    
    def addbefore(self,beforewhat,data):
        new_node=Node(data)
        if self.start==None:
            self.start=new_node
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
                
    ''' def deletebefore(self,beforewhat):
        if self.start==None:
            print("cant't delete")
        else:
            temp=self.start
            before=temp
            while temp!=None:
                if temp!=beforewhat:
                    before=temp
                    temp=temp.next
                else:
                '''

          
                    
            
                    
    def addstart(self,data):
        new_node=Node(data)
        if self.start==None:
            self.start=new_node
        else:
            temp=self.start
            self.start=new_node
            new_node.next=temp
    def deleteend(self):
        if self.start==None:
            print("How can i delete if list is empty")
        else:
            temp=self.start
            before=temp
            while temp.next!=None:
                before=temp
                temp=temp.next
            before.next=None


    def search(self,data):
        if self.start==None:
            print("How can i search..? list is empty")
        else:
            temp=self.start
            count=0
            while temp!=None:
                if temp.data!=data:
                    count+=1
                    temp=temp.next
                else:
                    print("element found at position:",count)
                    break


    def findvalue(self,index):
        if self.start==None:
            print("Mazak chalrha hai kya?")
        else:
            temp=self.start
            count=0
            while temp!=None:
                if count!=index:
                    count+=1
                    temp=temp.next
                else:
                    print("The value is:",temp.data)
                    break

        
                
                

                
                
mylist=linked_list()         
mylist.countnode()
mylist.insert(6)
mylist.insert(7)
mylist.insert(8)
mylist.insert(9)
mylist.traverse()
mylist.addstart(1)
mylist.countnode()
mylist.traverse()
mylist.addafter(1,2)
mylist.traverse()
mylist.deleteafter(6)
mylist.traverse()
mylist.addbefore(6,7)
mylist.traverse()
mylist.deleteend()
mylist.traverse()
mylist.search(1)
mylist.findvalue(3)


