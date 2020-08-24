class Queue:
    def __init__ (self):
        self.queue=[]
    def enque(self,data):
        self.queue.insert(0,data)
    def deque(self):
        r=self.queue.pop()
        return r
    def isempty(self):
        return self.queue==[]

q=Queue()
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
print(q.deque())
print(q.isempty())
print(q.deque())
print(q.deque())
print(q.deque())
print(q.isempty())
