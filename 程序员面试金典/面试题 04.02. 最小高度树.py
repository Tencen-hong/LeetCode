
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        nums.sort()
        return self.help(nums,0,len(nums)-1)

    def help(self,nums,l,r):
        if l==r:
            return TreeNode(nums[l])
        if l>r:
            return 
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = self.help(nums,l,mid-1)
        root.right = self.help(nums,mid+1,r)
        return root