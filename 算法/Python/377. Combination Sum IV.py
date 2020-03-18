class Solution:
    '''
    可以用动态规划来做, 也是一个背包问题, 求出[1, target]之间每个位置有多少种排列方式, 这样将问题分化为子问题. 状态转移方程可以得到为: dp[i] = sum(dp[i - nums[j]]),  (i-nums[j] > 0);
    如果允许有负数的话就必须要限制每个数能用的次数了, 不然的话就会得到无限大的排列方式, 比如1, -1, target = 1;
    '''

    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [1] + [0]*target
        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[-1]
