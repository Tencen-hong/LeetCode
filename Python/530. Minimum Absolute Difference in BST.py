# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    二叉搜索树，中序遍历结果即是递增序列
    找寻序列中相邻2点之间的 绝对差异 最小
    '''

    def getMinimumDifference(self, root: TreeNode) -> int:
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
