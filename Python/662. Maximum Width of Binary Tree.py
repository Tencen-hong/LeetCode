# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    用双端队列存储 节点和节点的位置
    res = 一层中最右节点位置-最左节点位置+1
    '''

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        curr = deque([(root, 0)])
        res = 0
        while curr:
            res = max(res, curr[-1][1]-curr[0][1]+1)
            for _ in range(len(curr)):
                t, pos = curr.popleft()
                if t.left:
                    curr.append((t.left, pos*2))
                if t.right:
                    curr.append((t.right, pos*2+1))
        return res
