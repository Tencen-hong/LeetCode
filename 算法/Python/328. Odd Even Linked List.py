# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        res, c1, c2 = ListNode(None), ListNode(None), ListNode(None)
        t1, t2 = c1, c2
        flag = True
        while head:
            if flag:
                t1.next = head
                t1 = t1.next
                flag = False
            else:
                t2.next = head
                t2 = t2.next
                flag = True
            head = head.next
        t1.next = c2.next
        t2.next = None
        res.next = c1.next
        return res.next
