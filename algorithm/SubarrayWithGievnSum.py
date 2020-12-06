def solveNonCont(a):
	a.sort()
	summ=0
	i=len(a)
	while(i>=0 ) and summ+a[i]>=summ:
		summ+=a[i]
		i-=1

	return summ

print(solveNonCont())