class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        i = 0
        while i<len(nums):
            if nums[i] != i+1 and nums[i]!=nums[nums[i]-1]:
                nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i]-1]
            elif nums[i] == i+1 or nums[i]==nums[nums[i]-1]:
                i+=1
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)

        return res
        '''

        return list(set(range(1, len(nums)+1)) - set(nums))
