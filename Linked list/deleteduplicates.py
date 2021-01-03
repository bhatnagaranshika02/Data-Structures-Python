class LLNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next
class Solution:
    def solve(self, node):
        seen = set()
        p = node
        curr = node
        while curr:
            if curr.val in seen:
                p.next = curr.next
            else:
                seen.add(curr.val)
                p = curr
            curr = curr.next
        return node
