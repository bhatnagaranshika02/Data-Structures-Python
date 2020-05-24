from stack1 import Stack
def reverse(s):
    for i in range(len(s)):
        stack.push(s[i])

    rev=''
    while not stack.isempty():
        rev+=stack.pop()

    return rev

stack=Stack()
s=input()
print(reverse(s))
