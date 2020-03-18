# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root = TreeNode(None)
        if not nums:
            return root

        def help(nums):
            if not nums:
                return
            root = TreeNode(max(nums))
            root_index = nums.index(root.val)
            root.left = help(nums[:root_index])
            root.right = help(nums[root_index+1:])

            return root

        root = help(nums)
        return root
