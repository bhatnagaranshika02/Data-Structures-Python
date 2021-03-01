l = list(map(int,input().split()))
for i in range(len(l)):
    flag = False
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            flag = True
            l[j],l[j+1] = l[j+1],l[j]

    if flag == False:
        print(l)
        quit()

print(l)
