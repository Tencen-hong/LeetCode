class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def help(A="", left=0, right=0):
            if len(A) == 2*n:
                res.append(A)
                return
            if left < n:
                help(A+'(', left+1, right)
            if right < left:
                help(A+')', left, right+1)

        res = list()
        help()

        return res
