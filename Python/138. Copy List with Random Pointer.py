"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    '''
        每个节点后面复制一个节点
        将复制的节点的random赋值
        分别用指针连接原链表和复制链表
    '''

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        p = head
        while p:
            t = Node(p.val, p.next, p.random)
            p.next = t
            p = p.next.next

        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        newHead = head.next
        pOld = head
        pNew = newHead
        while pNew.next:
            pOld.next = pNew.next
            pOld = pOld.next
            pNew.next = pOld.next
            pNew = pNew.next
        pOld.next = None
        pNew.next = None
        return newHead
