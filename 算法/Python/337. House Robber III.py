# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    分2种情况：1.rob当前节点，结果=当前节点值+当前节点的孙子节点值
             2.不rob当前节点，结果=当前节点的儿子节点值
    返回max(1,2)
    '''
    _map = {}
    def rob(self, root: TreeNode) -> int:

        if not root:
            return 0
        if self._map.get(root) is None:
            self._map[root] = max(
                root.val+self.robson(root.left)+self.robson(root.right), self.robson(root))
        return self._map[root]

    def robson(self, root):
        return self.rob(root.left) + self.rob(root.right) if root else 0
