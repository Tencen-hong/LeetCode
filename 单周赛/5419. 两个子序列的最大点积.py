class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        sz1 = len(nums1)
        sz2 = len(nums2)
        dp = [[-10000000 for j in range(sz2+1)] for i in range(sz1+1)]
        for i in range(1, sz1+1):
            for j in range(1, sz2+1):
                dp[i][j] = nums1[i-1] * nums2[j-1]
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + dp[i][j])
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                dp[i][j] = max(dp[i][j], dp[i][j-1])
                dp[i][j] = max(dp[i][j], dp[i-1][j-1])

        return dp[-1][-1]
