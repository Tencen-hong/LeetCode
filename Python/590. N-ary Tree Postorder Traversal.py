"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    '''
    1.将孩子节点从左到右压栈
    2.出栈，记录val,重复1,每次得到的顺序是 根->右->左
    3.最后翻转
    '''
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None:
            return res
        stack = [root]
        while stack:
            t = stack.pop()
            stack.extend(t.children)
            res.append(t.val)
        return res[::-1]
