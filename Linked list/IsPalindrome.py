class Node:
def __init__ (self,data):
	self.data = data
	self.next = next

class LinkedList:
	def __init__ (self):
		self.head = None

	def isPalindromeUtil(self,string):
            if string == string[::-1]:
                return 'Palindrome'
            else:
                return 'No Palindrome'
            
	def isPalindrome(self,data):
            if self.head is None:
                return None
            else:
                temp=[]
                temp2 = self.head
                while temp2 is not None:
                    temp.append(temp2.data)
                    temp2=temp2.next
                temp=''.join(temp)
                isPalindromeUtil(temp)
            
