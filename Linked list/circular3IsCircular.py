def is_circular(self,input_list):
    temp=self.head
    while temp.next:
        temp=temp.next
        if temp.next==self.head:
            return True
        else:
            return False
        
