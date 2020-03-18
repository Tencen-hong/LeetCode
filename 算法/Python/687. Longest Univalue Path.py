# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ret = 0

        def dfs(root, n):
            if not root:
                return 0
            left = dfs(root.left, root.val)
            right = dfs(root.right, root.val)
            self.ret = max(self.ret, left + right)
            return max(left, right) + 1 if root.val == n else 0
        dfs(root, 0)
        return self.ret
