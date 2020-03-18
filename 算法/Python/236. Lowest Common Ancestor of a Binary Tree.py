# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
        LCA 至少是(p,q)中靠近根节点的节点或其祖先，
        所以一旦发现p或q 节点就可以直接返回
        左子树and右子树都发现pq时LCA为当前节点
        只有单侧子树发现pq时LCA为单侧子树根节点

    '''

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right
