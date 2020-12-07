def Activity(s,f):
	n=len(f)
	j=0
	print(j)
	for i in range(1,n):
		if s[i]>=f[j]:
			print(i)
			j=i

s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 
Activity(s,f)

