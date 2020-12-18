class Node:
   def __init__(self, data): 
        self.data = data  
        self.next = None

class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    def deleteLastOccurence(self,x):
        if self.head==None:
            return
        else:
            temp = self.head
            tmp=0
            while temp:
                if temp.data == x:
                    tmp=x
                    temp=temp.next
           if tmp:
               del tmp
               return printlist(self.head)
