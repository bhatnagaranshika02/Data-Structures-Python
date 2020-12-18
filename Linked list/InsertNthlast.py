class Node:
def __init__ (self,data):
	self.data = data
	self.next = next

class LinkedList:
	def __init__ (self):
		self.head = None
	def LastNth(self,data,n):
            if self.head is None:
                return None
            else:
                temp=self.head
                count=0
                while temp:
                    count+=1
                    temp = temp.next
                n = count-n
                i=0
                temp=self.head
                prev=0
                while i!=n+1:
                    prev=temp
                    temp = temp.next
                prev.next = newnode
                newnode.next=temp
                
                
