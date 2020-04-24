class stack:
    def __init__ (self,max_size):
        self.__top = -1
        self.__max_size = max_size
        self.__elements=[None]* max_size

    def getmax(self):
        return self.__max_size
    def isfull(self):
        if len(self.__elements) > self.__max_size:
            return True
        else:
            return False
    def push(self,data):
        if self.isfull():
            print("stack is full")
        else:
            
            self.__elements[self.__top] = data
            self.__top+=1
            
    def show(self):
        return self.__elements
    def pop(self):
        if len(self.__elements)==0:
            print("Stack is empty")
        else:
            self.__top-=1
            popify=self.__elements.remove(self.__top)
            print("Popped element is ",popify)


obj1=stack(5)
print(obj1.getmax())
print(obj1.isfull())
obj1.push(7)
obj1.push(3)
obj1.pop()
obj1.push(2)
obj1.push(3)
obj1.push(0)
obj1.push(3)
print(obj1.isfull())
print(obj1.show())


