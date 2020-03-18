class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # recurrence
        ans = list()
        subset = list()

        def helper(subset, start):
            ans.append(subset[::])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                helper(subset, i+1)
                subset.pop()
        helper(subset, 0)
        return ans
