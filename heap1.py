import heapq
from heapq import merge
li=[5,7,9,1,3]
heapq.heapify(li)
print(list(li))
heapq.heappush(li,4)
print(list(li))
print(heapq.heappop(li))
print(heapq.heapreplace(li,8))
li2=[77,88,99]
m=merge(li,li2)
print(list(m))