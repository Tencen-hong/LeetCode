# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
        遍历顺序：右子树，根节点，左子树
        累加右子树的值
    '''

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.greater = 0
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.right)
        root.val += self.greater
        self.greater = root.val
        self.dfs(root.left)
