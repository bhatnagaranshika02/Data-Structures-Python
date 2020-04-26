A=list(map(int,input().split()))
for i in range(len(A)):
    minInd = i
    for j in range(i+1,len(A)):
        if A[minInd] > A[j]:
           minInd = j
    A[i],A[minInd] = A[minInd],A[i]
print(A)