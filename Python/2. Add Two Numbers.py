# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # to return res
        res = None
        # work node p
        p = res
        # carry
        carry = 0

        # do calculate when l1!=None or l2!=None or carry!=0
        while l1 or l2 or carry != 0:
            # add l1.val to carry
            if (l1):
                carry += int(l1.val)
                l1 = l1.next
            # add l2.val to carry
            if (l2):
                carry += int(l2.val)
                l2 = l2.next
            # if res is head node
            if (res == None):
                # create node carry%10  and move node p
                res = ListNode(int(carry % 10))
                p = res
            else:
                # create node carry%10  and move node p
                p.next = ListNode(int(carry % 10))
                p = p.next
            # make carry dropout single digit
            carry = int(carry / 10)

        return res
