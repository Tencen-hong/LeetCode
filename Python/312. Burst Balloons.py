class Solution:
    '''
    定义计算长度从1到n
    定义计算的边界范围i，j
    在当前情况下点爆k个气球，当作是最后一次被点爆,一共有k个选择，选取一个最大值
    '''
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0 for i in range(n + 2)] for j in range(n + 2)]

        for length in range(1, n + 1):
            for i in range(1, n - length + 1 + 1):
                j = i + length - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1]
                                   [j] + nums[i - 1] * nums[k] * nums[j + 1])

        return dp[1][n]
