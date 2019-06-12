# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    中序遍历单调递增
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        s = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            s.append(root.val)
            inOrder(root.right)

        inOrder(root)
        for i in range(1, len(s)):
            if s[i-1] >= s[i]:
                return False
        return True
