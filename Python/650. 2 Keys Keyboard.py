class Solution:
    '''
     算法有点类似筛法求素数,
     先把dp都设置为无穷大（inf）, 初始化条件为：dp[0]=dp[1]=0 ，若当前值为无穷大，则表示此数是素数，需要的step即为此素数。
     状态转移方程为： dp[i]=min(dp[i],dp[j]+i/j),i>1,j<i且i是j的整数倍
     上述状态转移方程表示：如果i是j的倍数，那么i可以通过粘贴(i/j-1)次j 得到, 再加上一次复制操作，那么可以通过dp[j]+i/j 次操作得到dp[i]

    '''

    def minSteps(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = dp[1] = 0
        for i in range(2, n+1):
            if dp[i] == float('inf'):
                dp[i] = i
            for j in range(i*2, n+1, i):
                dp[j] = min(dp[j], dp[i] + j//i)
            # print(dp)
        return dp[n]
