# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        cnt = 0
        p = pre = head
        nxt = None
        group = []

        def helper(node, group):
            q = None
            while node:
                t = node.next
                node.next = q
                q = node
                node = t
            group.append(q)

        while p:
            cnt += 1
            if cnt == k:
                nxt = p.next
                p.next = None
                helper(pre, group)
                p = pre = nxt
                cnt = 0
            else:
                p = p.next

        if 0 < cnt < k:
            group.append(pre)

        for i in range(len(group)-1):
            l = group[i]
            while l.next:
                l = l.next
            l.next = group[i+1]

        return group[0]
