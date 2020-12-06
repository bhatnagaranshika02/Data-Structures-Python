def subArraySum(arr,n,summ):
	curr_sum = arr[0]
	start=0
	i=1
	while i<=n:
		while curr_sum>summ and start < arr[i-1]:
			curr_sum = curr_sum - arr[start]
			start+=1

		if curr_sum == summ:
			print(summ)
		if i<n:
			curr_sum+=arr[i]
		i+=1

	print("No subarray found")
	return 0

arr = [15,2,4,8,9,5,10,23]
n=len(arr)
sum=23
subArraySum(arr,n,summ)