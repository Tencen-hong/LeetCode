# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    先序遍历，添加路径节点，遇到叶节点就保存路径
    '''

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []

        def preOrder(root, path):
            if not root:
                return
            path.append(str(root.val))
            if not root.left and not root.right:
                self.res.append(path.copy())
            preOrder(root.left, path)
            preOrder(root.right, path)
            path.pop()
        preOrder(root, [])
        self.res = ['->'.join(s) for s in self.res]
        return self.res
