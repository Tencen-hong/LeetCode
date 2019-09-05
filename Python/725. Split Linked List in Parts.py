# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length, cur = 0, root
        while cur:
            cur, length = cur.next, length + 1
        m, n = length//k, length % k
        res = [m+1]*n + [m]*(k-n)
        pre, cur = None, root
        for i, num in enumerate(res):
            if pre:
                pre.next = None
            res[i] = cur
            for _ in range(num):
                pre, cur = cur, cur.next

        return res
