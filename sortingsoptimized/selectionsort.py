l = list(map(int,input().split()))
for i in range(len(l)):
    mini = i
    for j in range(i+1,len(l)):
        if l[j]<l[mini]:
            mini = j

    l[mini],l[i] = l[i],l[mini]

print(l)
