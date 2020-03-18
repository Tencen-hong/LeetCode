

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        p = head
        p_kth = head
        idx = 0
        while p.next:
            idx += 1
            p = p.next
            if idx >= k:
                p_kth = p_kth.next
        return p_kth.val
    