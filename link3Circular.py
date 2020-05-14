class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

class Cirular:
    def __init__(self):
        self.last = None

    def addToEmpty(self,data):
        if (self.last!=None):
            return self.last
        temp=Node(data)
        self.last =temp
        self.last.next=self.last
        return self.last
