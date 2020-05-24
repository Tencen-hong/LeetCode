# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.Paths = []
        path = []
        self.preOrder(root, [])
        # print(self.Paths)
        res = 0
        for path in self.Paths:
            counter = collections.Counter(path)
            odd_num = 0
            for k, v in counter.items():
                if v % 2 == 1:
                    odd_num += 1
            if odd_num <= 1:
                res += 1
        return res

    def preOrder(self, root, path):

        path.append(root.val)
        if not root.left and not root.right:
            self.Paths.append(path.copy())
        if root.left:
            self.preOrder(root.left, path)
        if root.right:
            self.preOrder(root.right, path)
        path.pop()
