def heapify(l,n,i):
    largest = i
    left = 2* i+1
    right = 2* i+2
    if left<n and l[left] > l[largest]:
        largest = left
    if right<n and l[right] > l[largest]:
        largest = right
    if largest!=i:
        l[largest],l[i] = l[i],l[largest]
        heapify(l,n,largest)

def buildheap(li):
    for i in range(len(li)//2,-1,-1):
        heapify(l,len(l),i)

def heap_sort(l):
    for i in range(len(l)-1,-1,-1):
        l[0] , l[i] = l[i],l[0]
        heapify(l,i,0)

l = list(map(int,input().split()))
buildheap(l)
heap_sort(l)
print(l)

    
    
