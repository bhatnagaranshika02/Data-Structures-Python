from stack1 import Stack
s=Stack()
def parchecker(l):
    balanced=True
    i=0
    while i<len(l) and balanced==True:
        if l[i] in '([{':
            s.push(l[i])
        else:
            if s.isempty():
                balanced=False
            else:
                top=s.pop()
                if not matches(top,l[i]):
                    balanced=False
        i+=1
    if balanced==True:
        return True
    else:
        return False
def matches(open,close):
    opens = '{[('
    closer = ')]}'
    return opens.index(open)==closer.index(close)


print(parchecker('{{[[(())]]}}'))
