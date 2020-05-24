a=list(map(int,input().split()))
for i in range(len(a)-1):
    for j in range(i,len(a)-i-1):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print(a)