class Queue(object):
    def __init__ (self):
        self.items=[]
    def enqueue9self,value):
        self.items.insert(0,value)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class Binary_tree:
    def __init__(self,root):
        self.root=Node(root)

    def levelorder_traversal(self,start):
        if start==None:
            return
        else:
            queue=Queue()
            queue.enqueue(start)
            
            traversal=""

            while len(queue)>0:
                traversal+=str(queue.peek()) + '-'
                node=queue.dequeue()

                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return traversal
            












            
