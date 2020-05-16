class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None 

    def prepend(self, data):
        new_node = Node(data)
        temp=self.head
        new_node.next=self.head
        if not self.head:
            new_node.next=new_node

        else:
            while temp!=self.head:
                temp=temp.next
            else:
                temp.next=new_node
            self.head=new_node
            

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            

    def print_list(self):
        cur = self.head 

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
        print('\n')


    def remove(self,key):
        if self.head==None:
            print("List is None")
        else:
            temp=self.head
            before=temp
            while temp.next!=temp:
                if temp.data!=key:
                    before=temp
                    temp=temp.next
                else:
                    before.next=temp.next
                    break

    def __len__(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
            if temp==self.head:
                break
            return count

    def split(self):
        size=len(self)
        if size==0:
            return None
        if size==1:
            return self.head
        mid=size//2
        count=0

        prev=None
        temp=self.head

        while temp and count<mid:
            count+=1
            prev=temp
            temp=temp.next
            
        prev.next=self.head


    def joseph(self,step):
        temp=self.head
        while len(self)>1:
           count=1
           temp=self.head
           while count!=step:
               temp=temp.next
               count+=1
           print("Kill:"+str(temp.data))
           self.remove(temp)
           temp=temp.next

    def is_circular(self,input_list):
        temp=self.head
        while temp.next:
            temp=temp.next
            if temp.next==self.head:
                 return True
            else:
                 return False
        



c=CircularLinkedList()
c.append(3)
c.append(2)
c.append(4)
c.append(5)
c.append(6)
c.print_list()
c.remove(4)

c.print_list()
c.joseph(2)
c.print_list()
print(c.is_circular(c))




















            
