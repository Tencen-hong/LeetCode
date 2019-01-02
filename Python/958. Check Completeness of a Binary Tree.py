# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def level_traverse(root, level_order, index):
        if root and index < 300:
            level_order[index] = root.val
        if root.left:
            Solution.level_traverse(root.left, level_order, index*2)
        if root.right:
            Solution.level_traverse(root.right, level_order, index*2+1)

    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # The tree will have between 1 and 100 nodes.  => complete binary tree max_index < 300
        level_order = [-1 for i in range(300)]
        # Recursively build hierarchical traversal
        Solution.level_traverse(root, level_order, 1)

        # Null (ie -1) appears in the middle of the hierarchical traversal result, not a complete binary tree
        flag = 0
        for i in range(1, 300):
            if level_order[i] == -1:
                flag = 1
            if flag == 1 and level_order[i] != -1:
                flag = 2
                break

        if flag == 2:
            return False
        else:
            return True
