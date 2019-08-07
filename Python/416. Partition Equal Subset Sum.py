class Solution:
    '''
    和是奇数，不能分成2半
    递归查找是否能组成和的一半
    '''

    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        nums.sort(reverse=True)

        def helper(start, target):
            if (start, target) in cache:
                return cache[(start, target)]
            if target < 0:
                return
            elif target == 0:
                return True
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]):
                    return True
            cache[(start, target)] = False
            return False
        return False if sum(nums) % 2 else helper(0, sum(nums)/2)
