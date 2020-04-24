from pythonds.basic import Stack
def check(string):
    s=Stack()
    balanced = True
    index = 0
    while index < len(string):
        symbol = string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
print(check('((()))'))
print(check('(()'))
    
