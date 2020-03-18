class Solution:
    '''
        以i,j为正方形的右下角
        则i,j能构成正方形的个数为(i-1,j-1),(i-1,j),(i,j-1)中 最少的个数+1
    '''
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == 0:
                    continue
                dp[i][j] = min([dp[i-1][j-1], dp[i][j-1], dp[i-1][j]]) + 1
                res += dp[i][j]
        return res
