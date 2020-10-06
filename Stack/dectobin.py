stack=[]
def push(n):
    stack.append(n)
def pop():
    a=stack.pop()
    return a

def dec(dec_num):
    while dec_num > 0:
        result = dec_num%2
        push(result)

        dec_num//=2

    for i in stack:
        print(pop(),end='')


a=int(input())
dec(a)
    
