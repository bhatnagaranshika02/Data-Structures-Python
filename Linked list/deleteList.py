class Node:
   def __init__(self, data): 
        self.data = data  
        self.next = None

class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    def deleteList(self):
        temp= self.head
        while temp!=None:
            del temp.data
            temp=temp.next

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head  
        self.head = new_node

if __name__ == '__main__': 
  
    llist = LinkedList() 
    llist.push(1) 
    llist.push(4) 
    llist.push(1) 
    llist.push(12) 
    llist.push(1) 
  
  
    print("Deleting linked list") 
    llist.deleteList() 
      
    print("Linked list deleted") 
            
