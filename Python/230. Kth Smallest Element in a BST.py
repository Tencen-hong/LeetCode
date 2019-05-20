# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def size(self, root):
        if not root:
            return 0
        return self.size(root.left) + self.size(root.right) + 1

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        left_size = self.size(root.left)
        if left_size == k-1:
            return root.val
        elif left_size > k-1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - left_size - 1)
