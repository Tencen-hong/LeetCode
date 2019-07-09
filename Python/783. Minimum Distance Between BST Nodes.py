# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        inorder = []

        def inOrder(root):
            if root:
                inOrder(root.left)
                inorder.append(root.val)
                inOrder(root.right)
        inOrder(root)
        result = inorder[-1]
        for i in range(1, len(inorder)):
            if inorder[i] - inorder[i-1] < result:
                result = inorder[i] - inorder[i-1]

        return result
