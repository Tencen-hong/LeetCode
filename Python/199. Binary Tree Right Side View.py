# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    层次遍历，取每层最右侧的节点
    '''

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(1, length+1):
                t = queue.pop(0)
                if i == length:
                    res.append(t.val)
                if t.left:
                    queue.append(t.left)
                if t.right:
                    queue.append(t.right)
        return res
