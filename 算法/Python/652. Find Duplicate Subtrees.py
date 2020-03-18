# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    记录以每个节点为开始时的先序遍历（中左右）的数值，然后遍历的序列如果重复出现了，那么就自然可以加入了
    '''

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = collections.Counter()
        res = []

        def helper(node):
            if not node:
                return '#'
            serial = '{},{},{}'.format(
                node.val, helper(node.left), helper(node.right))
            count[serial] += 1
            if count[serial] == 2:
                res.append(node)
            return serial

        helper(root)
        return res
