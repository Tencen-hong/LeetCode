# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        d = {}

        def preOrder(root):
            if root:
                d[root.val] = d.get(root.val, 0) + 1
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)
        max_v = max(d.values())
        return [k for k, v in d.items() if v == max_v]
