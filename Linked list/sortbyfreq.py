def sortByFreq(arr,n):
    maxE=-1;
    for i in range(n):
        maxE=max(maxE,arr[i])
    freq=[0]*(maxE+1)
    for i in range(n):
        freq[arr[i]]+=1

    cnt=0
    for i in range(maxE+1):
        if (freq[i]>0):
            value=100000-i
            arr[cnt]=100000*freq[i]+value
            cnt+=1
    return cnt

def printsorted(arr,cnt):
    for i in range(cnt):
        frequency=arr[i]/100000
        value=100000-(arr[i]%100000)
        for j in range(int(frequency)):
            print(value,end=" ")

arr = [ 4, 4, 5, 6, 4, 2, 2, 8, 5 ]
n = len(arr)
cnt = sortByFreq(arr, n);
arr.sort(reverse = True)
printsorted(arr, cnt);

















l=list(map(int,input().split()))

    
