l = list(map(int,input().split(' ')))
swapped = True
while swapped:
    swapped =False
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
            swapped =True

print(l)
