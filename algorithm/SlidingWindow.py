def maxSum(arr,k):
	if len(arr)<k:
		return "Invalid"
		return -1
	window_sum = sum(arr[:k])
	max_sum = window_sum

	for i in range(n-k):
		window_sum=window_sum-arr[i]+arr[i+1]
		max_sum = max(window_sum,max_sum)
	return max_sum

print(maxSum([1,4,2,10,2,3,1,0,20]),4)