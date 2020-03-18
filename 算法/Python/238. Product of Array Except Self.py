class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        temp = 1
        for i in range(len(nums)):
            res[i] = temp
            temp = temp*nums[i]

        temp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*temp
            temp = temp*nums[i]
        return res
