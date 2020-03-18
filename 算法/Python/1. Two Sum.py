class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mmap = {}

        for indices, value in enumerate(nums):
            if target - value in mmap:
                return [mmap[target - value], indices]
            else:
                mmap[value] = indices

        return