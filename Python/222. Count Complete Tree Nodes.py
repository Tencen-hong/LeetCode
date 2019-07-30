# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    如果左树高，则加上右树的结点，继续进行探索左树。
    如果右树高或者等高，则加上左树的结点数，继续探索右树。
    '''

    def countNodes(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return 0
        p = root
        while p:
            left = self.help(p.left)
            right = self.help(p.right)
            if left > right:
                ans += 1 << right
                p = p.left
            else:
                ans += 1 << left
                p = p.right
        return ans

    def help(self, root):
        cnt = 0
        while root:
            cnt += 1
            root = root.left
        return cnt
