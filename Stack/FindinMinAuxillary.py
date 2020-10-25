from collections import deque
class MinStack:
    def __init__ (self):
        self.s = deque()
        self.aux = deque()

    def push(self,x):
        self.s.append(x)

        if not self.aux:
            self.aux.append(x)

        elif self.aux[-1]>=x:
            self.aux.append(x)

        else:
            pass

    def pop(self):
        
        if self.empty():
            print("Stack underflow")
            return -1

        top = self.s.pop()
        if top == self.aux[-1]:
            self.aux.pop()

        return top

    def peek(self):
        return self.s[-1]

    def len(self):
        return self.len(s)

    def empty(self):
        return not self.s

    def min(self):
        if not self.aux:
            print("Stack underflow")
            return -1
        return self.aux[-1]


if __name__ == 'main':
    s = MinStack()
    s.push(6)
    print(s.min())  # prints 6

    s.push(7)
    print(s.min())  # prints 6

    s.push(8)
    print(s.min())  # prints 6

    s.push(5)
    print(s.min())  # prints 5

    s.push(3)
    print(s.min())  # prints 3

    s.pop()
    print(s.min())  # prints 5

    s.push(10)
    print(s.min())  # prints 5
















        
