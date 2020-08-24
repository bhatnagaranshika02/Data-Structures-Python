s = input()
n=-1
while len(s)!=n:
    n =len(s)
    s=s.replace('()','')
    s=s.replace('[]','')
    s=s.replace('{}','')
if len(s)==0:
    print("Yes")
else:
    print("No")
