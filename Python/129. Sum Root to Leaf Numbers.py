# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    找出所有到叶节点的路径
    计算每条路径的数值
    累加所有路径
    '''

    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = []

        def getPath(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                self.ans.append(int(path))
            getPath(root.left, path)
            getPath(root.right, path)
            path = path[:-1]
        getPath(root, '')
        return sum(self.ans)
