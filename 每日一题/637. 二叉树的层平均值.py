# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ret = []
        q = [root]
        while(len(q)):
            size = len(q)
            temp_sum = 0
            for i in range(size):
                top = q.pop(0)
                temp_sum += top.val
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            ret.append(temp_sum/size)
        return ret
