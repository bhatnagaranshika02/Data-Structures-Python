def middle(self,head):
    if(head==None):
        return head
    slow=head
    fast=head
    while fast.next!None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next

    return slow
