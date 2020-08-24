
    

def total(root):
    if root is None:
        return False
    return total(root.left)+total(root.right) + 1

def totalinternal(root):
    if root is None:
        return 0
    if root.left is None:
        if root.right is None:
            return 0
    return totalinternal(tree.left)+totalinternal(tree.right) +1

def totalextrenal(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return totalexternal(root.left)+totalexternal(root.right)
