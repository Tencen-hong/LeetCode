"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    '''
    1.将孩子节点都从右向左压栈
    2.每次出栈记录val，再重复1
    '''

    def preorder(self, root: 'Node') -> List[int]:
        s = [root]
        res = []
        if root == None:
            return res
        while s:
            t = s.pop(-1)
            res.append(t.val)
            for i in range(len(t.children)-1, -1, -1):
                s.append(t.children[i])
        return res
