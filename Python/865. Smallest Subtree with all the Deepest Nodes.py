# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.res = None
        self.maxdepth = 0

        def dfs(root, depth):
            if(root == None):
                return depth
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)
            if(left == right and left >= self.maxdepth):
                self.maxdepth = left
                self.res = root
            return max(left, right)
        dfs(root, 0)
        return self.res
