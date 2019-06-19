class Solution:
    '''
    动态规划
    新值等于min(左边的值，上边的值)+原值
    '''

    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0] = grid[0][0]
        for j in range(1, len(dp[0])):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            for j in range(1, len(dp[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        print(dp)
        return dp[-1][-1]
