from stack1 import Stack
def convert(n):
    while n>0:
        rem=n%2
        stack.push(rem)
        n=n//2
    bin_num=''
    while not stack.isempty:
        bin_num+=str(stack.pop())
    return bin_num


stack=Stack()
n=int(input())
d=convert(n)
print(d)
