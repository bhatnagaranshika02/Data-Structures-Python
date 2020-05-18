#Time complexity: o(n)


def find_fixed(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None


#Time complexity: o(log n)
def find_fixed2(A):
    low=0
    high=len(A)-1

    while low<=high:
        mid =(low+high)//2
        if A[mid]<mid:
            low=mid+1

        elif A[mid]>mid:
            high=mid-1
        else:
            return A[mid]
    return None


# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]
print("Linear Approach")
print(A1)
print(find_fixed(A1))
print(A2)
print(find_fixed(A2))
print(A3)
print(find_fixed(A3))
print("\nBinary Search Approach")
print(A1)
print(find_fixed2(A1))
print(A2)
print(find_fixed2(A2))
print(A3)
print(find_fixed2(A3))
