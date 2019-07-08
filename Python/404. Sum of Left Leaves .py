# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.result = 0

        def preOrder(root):
            if root:
                if root.left and not root.left.left and not root.left.right:
                    self.result += root.left.val
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return self.result
