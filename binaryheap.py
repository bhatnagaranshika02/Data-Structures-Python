def heapify(arr,n,i):
	largest =i
	l=2*i +1
	r=2*i +2

	if l<n and arr[i]<arr[l]:
		largest = l
	if r<n and arr[largest]<arr[r]:
		largest = r

	if largest!=i:
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify(arr,n,largest)

def insert(arr,i):
	if len(arr) == 0:
		arr.append(i)
	else:
		arr.append(i)
		for num in range(len(arr)//2 , -1,-1):
			heapify(arr,len(arr),num)

def deleteNode(arr,i):
	if len(arr) ==0:
		return 
	for num in range(len(arr)):
		if num == i:
			break
	arr[num],arr[len(arr)-1] = arr[num],arr[len(arr)-1]
	arr.remove(i)

	for i in range((len(arr)//2)-1, -1, -1):
		heapify(arr, len(arr), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
