# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    result = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        self.dfs(root, sum)
        return self.result

    def dfs(self, root, sum):
        if not root:
            return
        if root.val == sum:
            self.result += 1
        self.dfs(root.left, sum-root.val)
        self.dfs(root.right, sum-root.val)
