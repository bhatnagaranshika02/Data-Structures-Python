
def remove_node(self, node):
  if self.head == node:
    cur = self.head 
    while cur.next != self.head:
      cur = cur.next
    if self.head == self.head.next:
      self.head = None
    else:
      cur.next = self.head.next 
      self.head = self.head.next
  else:
    cur = self.head 
    prev = None
    while cur.next != self.head:
      prev = cur 
      cur = cur.next 
      if cur == node:
        prev.next = cur.next
        cur = cur.next

def joseph(self,step):
    temp=self.head
    while len(self)>1:
        count=1
        while count!=step:
            temp=temp.next
            count+=1
        print("Kill:"+str(temp.data))
        self.remove_node(temp)
        temp=temp.next
