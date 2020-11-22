W = int(input())
Values = list(map(int,input().split()))
weights = list(map(int,input().split()))
l=[]
l= {Values[i]/weights[i]:(Values[i],weights[i]) for i in range(len(Values))}
profit=0
for key,value in sorted(l.items()):
    if value[1] <= W:
        W-=value[1]
        profit+=value[0]
    elif value[1]>W and W!=0:
        profit+=(W/value[1])*value[0]

        W=0

print(profit)
