from stack1 import Stack
stack = Stack()
def toStr(n,base):
    convertstring = "01234567"
    while n>0:
        if n<base:
            stack.push(covertstring[n])
        else:
            stack.push(convertstring[n%base])
        
            
