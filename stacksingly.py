class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class stacklink:
    def __init__(self):
        self.start=None


    def push(self,data):
        new_node= Node(data)
        if self.start==None:
            self.start=new_node
            new_node.next=None
        else:
            temp=self.start
            while temp!=None:
                if temp.next!=None:
                    temp=temp.next
                
                else:
                    temp.next=new_node
                    new_node.next=None
                    break

    def pop(self):
        temp=self.start
        before=temp
        data=0
        while temp:
            before=temp
            temp=temp.next
            if temp.next==None:
                data=temp.data
                before.next=None
                break


    def peek(self):
        temp=self.start
        return temp.data


    def isEmpty(self):
        if self.start==None:
            return True
        else:
            return False
        
           
    def traverse(self):
        temp=self.start
        while temp!=None:
            print(temp.data)
            temp=temp.next
        print('\n')
        

s=stacklink()
s.push(1)
s.push(2)
s.traverse()
s.push(3)
s.push(4)
s.traverse()
s.pop()
s.traverse()
s.pop()
s.traverse()
print(s.peek())
s.traverse()


