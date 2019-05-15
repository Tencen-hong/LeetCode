# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        inorder = []

        def inOrder(root):
            if(root == None):
                return
            inOrder(root.left)
            inorder.append(root.val)
            inOrder(root.right)
        inOrder(root)

        l, r = 0, len(inorder)-1
        while l < r:
            if inorder[l]+inorder[r] == k:
                return True
            elif inorder[l]+inorder[r] > k:
                r -= 1
            elif inorder[l]+inorder[r] < k:
                l += 1
        return False
