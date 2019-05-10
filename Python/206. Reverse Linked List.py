# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        return self._reverse(head)

        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        p = node.next
        node.next = prev
        return self._reverse(p, node)
