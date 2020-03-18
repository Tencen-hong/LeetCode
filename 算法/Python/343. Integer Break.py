class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans = 0
        for i in range(2, n+1):
            piece_num = int(n/i)
            extra = int(n % i)
            temp_max = int(pow(piece_num, i-extra) * pow(piece_num+1, extra))
            if temp_max > ans:
                ans = temp_max
        ans = int(ans)
        return ans
