class Solution:
    def equals(s, t):
        if(s == None and t == None):
            return True
        if s == None or t == None:
            return False
        return s.val == t.val and Solution.equals(s.left, t.left) and Solution.equals(s.right, t.right)

    def traverse(s, t):
        return s != None and (Solution.equals(s, t) or Solution.traverse(s.left, t) or Solution.traverse(s.right, t))

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if s == None and t == None:
            return True

        return Solution.traverse(s, t)
