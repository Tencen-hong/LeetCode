class Solution:
    '''
    dp[] 维护以x结尾的最长字符串的长度
    dz[] 维护以x结尾的最长字符串的个数
    '''

    def findNumberOfLIS(self, nums: List[int]) -> int:
        maxLIS = ans = 0
        size = len(nums)
        dp = [1]*size
        dz = [1]*size
        for x in range(size):
            for y in range(0, x):
                if nums[y] < nums[x]:
                    if dp[y] + 1 > dp[x]:
                        dp[x] = dp[y] + 1
                        dz[x] = dz[y]
                    elif dp[y] + 1 == dp[x]:
                        dz[x] += dz[y]
        maxLIS = max(dp + [0])  # [0] 解决nums空集情况
        for p, z in zip(dp, dz):
            if p == maxLIS:
                ans += z
        return ans
