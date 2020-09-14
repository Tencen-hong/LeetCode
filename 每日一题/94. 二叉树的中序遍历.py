# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stk = []
        ret = []
        while root or len(stk) > 0:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            ret.append(root.val)
            root = root.right

        return ret
