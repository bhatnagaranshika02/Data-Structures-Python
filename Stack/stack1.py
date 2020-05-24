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

