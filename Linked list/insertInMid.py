class Node:
def __init__ (self,data):
	self.data = data
	self.next = next

class LinkedList:
	def __init__ (self):
		self.head = None

	def InsertMid(self,data):
            newnode=Node(data)
            if self.head is None:
                return None
            temp = self.head
            l=[]
            while temp is not None:
                temp=temp.next
                l+=1
            break
            prev=0
            if l%2==0:
                count=l//2
            else:
                count = (l+1)//2
            temp = self.head

            while count>1:
                count-=1
                prev=temp
                temp = temp.next
            prev.next = newnode
            newnode = temp
            
