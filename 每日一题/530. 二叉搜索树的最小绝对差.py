# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = float('inf')
        self.pre = -1

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.pre == -1:
                self.pre = root
            else:
                self.ans = min(self.ans, root.val-self.pre.val)
                self.pre = root
            dfs(root.right)

        dfs(root)
        return self.ans
