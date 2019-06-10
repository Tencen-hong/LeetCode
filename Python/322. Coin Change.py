class Solution:
    '''
    我们用到的样例是面值数组coins=[2, 5, 1], 总额amount = 11，此时n=3， m=11；我们用dp[m][n]来表示所有可能的状态，dp[i][j]表示，用前i(0 <= i < n)个面值，表示总额j(0 <= j <= m)，需要纸币的最少数目。
    j=0，就是要组成的总额为0时，就是j最基本的问题了，很明显，需要0张2，0张5，0张1也就是说dp[i][0] = 0 (0 <= i < n);
    在某个面值做选择时，只有两种可能，我用这个面值，和我不用这个面值：
    我用这个面值，就和前面一样了：
    dp[i][j] = dp[i][j - coins[i]] + 1;
    我不用这个面值，那我就直接继承之前的状态：
    dp[i][j] = dp[i - 1][j];
    总共就这两种可能，我就选个最小的就好了，因为答案需要最少的数量嘛，所以这一步的转移方程：
    dp[i][j] = min(dp[i][j - coins[i]] + 1, dp[i - 1][j]);

    将dp优化成一维数组
    '''

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if j-coins[i] >= 0:
                    dp[j] = min(dp[j], dp[j-coins[i]]+1)
        if dp[-1] >= float('inf'):
            return -1
        else:
            return dp[-1]
