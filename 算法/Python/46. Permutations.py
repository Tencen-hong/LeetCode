class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()

        def help(nums, begin):
            if(begin >= len(nums)):
                res.append(nums)
                return
            for i in range(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                help(nums[::], begin+1)
                nums[i], nums[begin] = nums[begin], nums[i]

        help(nums, 0)
        return res
