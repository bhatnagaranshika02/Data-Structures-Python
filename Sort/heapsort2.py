def heapify(arr,n,i):
    largest = i
    left = 2* i+1
    right= 2* i+2

    if left<n and arr[left] > arr[largest]:
        largest = left
    if right<n and arr[right]>arr[largest]:
        larget = right
    if largest!=i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)


def buildheap(li):
    for i in range(len(li)//2,-1,-1):
        heapify(l,len(l),i)

def heapsort(l):
    for i in range(len(l)-1,-1,-1):
        l[0],l[i] = l[i],l[0]
        heapify(l,i,0)



l = list(map(int,input().split()))
buildheap(l)
heapsort(l)
print(l)
