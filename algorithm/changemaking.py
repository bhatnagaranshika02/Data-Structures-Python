def change(n,coins_available,coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far

    elif sum(coins_so_far) > n:
        pass
    elif coins_available ==[]:
        pass
    else:
        for c in change(n,coins_available[:],coins_so_far+[coins_available[0]]):
            yield c
        for c in change(n,coins_available[1:],coins_so_far):
            yield c
n = int(input("enter the value of n: "))
coins=[1,5,10,25]

s = [s for s in change(n,coins,[])]
for i in s:
    print(i)
print("optimal solution:",min(s,key=len))
