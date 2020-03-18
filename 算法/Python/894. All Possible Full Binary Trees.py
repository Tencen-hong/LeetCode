# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    显然，对于完全二叉树的每一个结点，要么它是一个叶结点，要么它的左右子树都是完全二叉树。而且显然完全二叉树的结点数目必然是奇数。于是我们可以通过递归解决这个问题：对于要求的结点总数N，枚举所有可能的左子树结点数（i，奇数）以及对应的右子树结点数（N - i - 1），然后把生成的子树拼在一起，得到所有可能的拼法。可以将N对应的所有树存起来，减少迭代的次数。
    '''

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        N -= 1
        if N == 0:
            return [TreeNode(0)]
        ret = []
        for i in range(1, N, 2):
            for _left in self.allPossibleFBT(i):
                for _right in self.allPossibleFBT(N-i):
                    root = TreeNode(0)
                    root.left = _left
                    root.right = _right
                    ret.append(root)
        return ret
