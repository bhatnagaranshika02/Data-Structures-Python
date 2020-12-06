def MaxSubarray(a,size):
	max_so_far = 0
	max_ending_here=0

	for i in range(0,size):
		max_ending_here +=arr[i]
		if max_ending_here<0:
			max_ending_here=0
		elif(max_so_far<max_ending_here):
			max_so_far=max_ending_here
	return max_so_far

def maxSubarray2(a,size):
	max_so_far = a[0]
	curr_max = a[0]

	for i in range(1,size):
		curr_max = max(a[i],curr_max+a[i])
		max_so_far=max(max_so_far,curr_max)
	return max_so_far


print(MaxSubarray([1,3,4,5,74,8],6))
print(maxSubarray2([1,3,4,5,74,8],6))