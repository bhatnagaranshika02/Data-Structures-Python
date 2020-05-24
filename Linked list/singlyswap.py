def swap_nodes(self,key1,key2):
    if key1==key2:
        return
    prev1=None
    temp=self.head
    while temp and temp.data!=key1:
        prev1=temp
        temp=temp.next

    prev2=None
    temp2=self.head
    while temp2 and temp2.data!=key2:
        prev2=temp
        temp=temp.next
    if not key1 or not key2:
        return
    if key1:
        prev1.next=temp2
    else:
        self.head=temp2

    if key2:
        prev2.next=temp
    else:
        self.head=temp

    temp.next,temp2.next=temp2.next
    
