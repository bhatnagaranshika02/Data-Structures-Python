def integer_square_root(k):
    low=0
    high=k

    while low<=k:
        mid=(low+high)//2
        mid_square=mid*mid
        if mid_square<=k:
            low=mid+1
        else:
            high=mid-1
    return low-1

k=300
print(integer_square_root(k))
