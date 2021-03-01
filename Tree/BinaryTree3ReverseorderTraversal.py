class Queue(object):
    def __init__ (self):
        self.items=[]
    def enqueue(self,value):
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
    

class stack:
    def __init_-(self):
        self.items=[]

    def push(self,value):
        self.items.append(value)
        
    def pop(self):
        if not self.is_empty:
            return self.items.pop()


class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class Binary_tree:
    def __init__(self,root):
        self.root=Node(root)

    def reverse_levelorder(self,start):
        if start is None:
            return
        queue=Queue()
        stack=Stack()
        queue.enqueue(start)

        traversal=''
        while len(queue)>0:
            node=queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

            while len(stack)>0:
                node=stack.pop()
                traversal+=str(node.value)+'-'

        return traversal
            






















        
            

