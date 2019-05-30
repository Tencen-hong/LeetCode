# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        stack, zigzag = [[], []], 0
        stack[zigzag].append(root)
        res = []
        while stack[zigzag]:
            temp = []
            while stack[zigzag]:
                top = stack[zigzag].pop(-1)
                temp.append(top.val)
                if zigzag == 1:
                    if top.right:
                        stack[1-zigzag].append(top.right)
                    if top.left:
                        stack[1-zigzag].append(top.left)
                else:
                    if top.left:
                        stack[1-zigzag].append(top.left)
                    if top.right:
                        stack[1-zigzag].append(top.right)
            res.append(temp.copy())
            zigzag = 1-zigzag
        return res
