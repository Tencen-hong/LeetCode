# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        if d == 1:
            t = TreeNode(v)
            t.left = root
            return t

        def helper(root, v, d, depth):
            if not root:
                return

            if d == depth+1:
                t1 = TreeNode(v)
                t1.left = root.left
                root.left = t1
                t2 = TreeNode(v)
                t2.right = root.right
                root.right = t2
                return
            helper(root.left, v, d, depth+1)
            helper(root.right, v, d, depth+1)

        helper(root, v, d, 1)
        return root
