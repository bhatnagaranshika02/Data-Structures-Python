def reverse(self):
    tmp=None
    temp=self.head
    while temp:
        tmp=temp.prev    #None
        temp.prev=temp.next
        temp.next=prev
        
