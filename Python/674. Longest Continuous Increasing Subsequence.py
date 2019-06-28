class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ret = 0
        temp_length = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp_length += 1
                ret = max(ret, temp_length)
            else:
                temp_length = 1
        return max(ret, temp_length)
