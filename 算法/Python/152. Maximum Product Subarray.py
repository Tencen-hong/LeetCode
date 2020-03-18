class Solution:
    '''
    维护一局部最大和一个局部最小
    最大值出现在 (局部最大*当前数，局部最小*当前数，当前数) 之中
    '''

    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        max_local = nums[0]
        min_local = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            max_copy = max_local
            max_local = max(nums[i]*max_local, nums[i], nums[i]*min_local)
            min_local = min(nums[i], nums[i]*min_local, nums[i]*max_copy)
            res = max(res, max_local)
        return res
