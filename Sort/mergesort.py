def MergeSort(array, left,right):
    if left<right:
        mid = (right+left)/2
        MergeSort(array,left,right)
        MergeSort(array,mid+1,end)
        Merge(array,start,mid,end)


def Merge(array,left,mid,right):
    i = start
    j=mid+1
    index=start
    temp = []*10
    while(i<=mid and j<=right):
        
    
