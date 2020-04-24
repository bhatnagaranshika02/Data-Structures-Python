class Stack:
    def __init__(self):
        self.stacky=[]
    def isempty(self):
        return self.stacky == []
    def push(self,data):
        self.stacky.append(data)
    def pop(self):
        g=self.stacky.pop()
        return g
    def peek(self):
        self.stacky.pop(0)
    def size(self):
        return len(self.stacky)

s=Stack()
print(s.isempty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isempty())
s.push(8.4)
g=s.pop()
print(g)
print(s.size())
