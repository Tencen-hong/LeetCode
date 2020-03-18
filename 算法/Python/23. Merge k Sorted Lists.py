# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for line in lists:
            while line:
                heapq.heappush(heap, line.val)
                line = line.next
        res = ListNode(None)
        p = res
        while heap:
            t = heapq.heappop(heap)
            t = ListNode(t)
            p.next = t
            p = t
        return res.next
