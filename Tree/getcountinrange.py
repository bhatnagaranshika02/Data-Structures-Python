def getcount(root,low,high):
    if root == None:
        return 0
    if root.data == high and root.data == low:
        return 1
    if root.data <= high and root.data >=low:
        return (1+getcount(root.left,low,high) + getcount(root.right,low,high))
    elif root.data < low:
        return getcount(root.right,low,high)
    else:
        return getcount(root.left,low,high)
