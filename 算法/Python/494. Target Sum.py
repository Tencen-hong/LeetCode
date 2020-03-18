class Solution:
    '''
    举例说明: nums = {1,2,3,4,5}, target=3, 一种可行的方案是+1-2+3-4+5 = 3
        该方案中数组元素可以分为两组，一组是数字符号为正(P={1,3,5})，另一组数字符号为负(N={2,4})
        因此: sum(1,3,5) - sum(2,4) = target
          sum(1,3,5) - sum(2,4) + sum(1,3,5) + sum(2,4) = target + sum(1,3,5) + sum(2,4)
          2sum(1,3,5) = target + sum(1,3,5) + sum(2,4)
          2sum(P) = target + sum(nums)
          sum(P) = (target + sum(nums)) / 2
    由于target和sum(nums)是固定值，因此原始问题转化为求解nums中子集的和等于sum(P)的方案个数问题

    dp[9] = dp[9] + dp[9-3] 表示子集和为9时方案的个数 = 原值+子集和为6的方案个数
    从nums中每增加一个数，从dp[S]到dp[nums[i]] 更新一轮dp,
    返回dp[S]

    '''

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        _sum = sum(nums)
        if S > _sum or (_sum+S) % 2 == 1:
            return 0

        return self.subsetSum(nums, (_sum+S)//2)

    def subsetSum(self, nums, S):
        dp = [0]*(S+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(S, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]

        return dp[S]
