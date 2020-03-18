# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    '''
    归并排序
    设定快速移动的指针和慢速移动的指针，分割前一半和后一半
    合并2个链表
    '''

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def merge(a, b):
            dum = ListNode(0)
            p = dum
            while a or b:
                if not a:
                    p.next, b = b, b.next
                elif not b:
                    p.next, a = a, a.next
                elif a.val < b.val:
                    p.next, a = a, a.next
                else:
                    p.next, b = b, b.next
                p = p.next
            return dum.next

        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        second = slow.next
        slow.next = None
        return merge(self.sortList(head), self.sortList(second))
