from pythonds.basic import Deque
def palchecker(string):
    chardeque = Deque()
    for i in string:
        chardeque.addRear(i)
    stillEqual =1
    while chardeque.size > 1 and stillEqual==1:
        first = chardeque.removeFront()
        last=chardeque.removeRear()
        if first!=last:
            stillEqual = 0
    return stillEqual

print(palchecker('lsdkjfskf'))
print(palchecker('ksdsgdjs'))
