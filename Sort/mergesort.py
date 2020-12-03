def merge_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        mid = len(arr)//2
        left,right = merge_sort(arr[:mid]),merge_sort(arr[mid:])
        return merge(left,right,arr.copy())


def merge(left,right,merged):
    left_cur,right_cur = 0,0
    while left_cur<len(left) and right_cur<len(right):
        if left[left_cur] <= right[right_cur]:
            
