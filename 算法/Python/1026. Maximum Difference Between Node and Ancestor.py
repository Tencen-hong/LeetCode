# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, max_, min_):
            if not node:
                return 0
            max_ = max(max_, node.val)
            min_ = min(min_, node.val)
            l = dfs(node.left, max_, min_)
            r = dfs(node.right, max_, min_)

            return max(max_-min_, l, r)

        return dfs(root, root.val, root.val)
