# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        self.count = collections.Counter()

        def dfs(node):
            if node == None:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.count[s] += 1
            return s

        dfs(root)
        maxCount = max(self.count.values())
        return [v for v in self.count if self.count[v] == maxCount]
