class Node(object):
    def __init__ (self,data=None,next_node=None,prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node=prev_node



def sortedInserted(head,data):
    node = Node(data,None,None)
    if (head==None):
        return None
    elif (data < head.data):
        node.next =  head
        head.prev = node
        return node
    else:
        node = sortedInserted(head.next , data):
        head.next= node
        node.prev = head
        reutrn head

for i in range(int(input())):
    l.append(int(input()))
    
