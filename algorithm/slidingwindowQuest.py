l = list(map(int,input().split()))
K,X=map(int,input().split())
summ=0
for i in range(0,K):
    summ+=l[i]
if summ<X:
    curr_max=summ
else:
    curr_max=0

for i in range(K,len(l)):
    summ = summ - l[i-K]+l[i]
    if summ<X:
        curr_max = max(curr_max,summ)
print(curr_max)    