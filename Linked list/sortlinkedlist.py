class Solution:
    def solve(self, node):
        nums = []

        ptr = node
        while ptr:
            nums.append(ptr.val)
            ptr = ptr.next

        ptr = node
        nums.sort(reverse=True)

        while ptr:
            ptr.val = nums.pop()
            ptr = ptr.next

        return node
