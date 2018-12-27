class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dynamic Programming
        if len(nums) == 0:
            return 0

        num_count = collections.Counter(nums)
        # value store num and corresponding value
        value = collections.defaultdict(int)
        for num in num_count.elements():
            value[num] = num*num_count[num]

        # dp store max_value before index i(include i)
        dp = [0 for _ in range(max(nums)+10)]
        dp[0] = value[0]
        dp[1] = value[1]

        for i in range(2, max(nums)+10):
            # current value is the max between the value before and the value 2 position in front of current.   like  1-2 Stair climbing problem
            dp[i] = max(dp[i-2] + value[i], dp[i-1])

        return dp[-1]
