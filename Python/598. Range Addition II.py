class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        a, b = m, n
        for x, y in ops:
            a = min(a, x)
            b = min(b, y)
        return a*b
