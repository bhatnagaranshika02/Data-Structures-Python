class LLNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next
class Solution:
    def solve(self, node):
        curr=node
        while curr and curr.next:
            curr.val,curr.next.val=curr.next.val,curr.val
            curr=curr.next.next
        return node
