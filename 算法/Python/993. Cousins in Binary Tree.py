# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = []
        queue.append(root)
        parents = set()
        while queue:
            size = len(queue)
            parents.clear()
            while size > 0:
                size -= 1
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                    if temp.left.val in [x, y]:
                        parents.add(temp)
                if temp.right:
                    queue.append(temp.right)
                    if temp.right.val in [x, y]:
                        parents.add(temp)
            if len(parents) == 2:
                return True
        return False
