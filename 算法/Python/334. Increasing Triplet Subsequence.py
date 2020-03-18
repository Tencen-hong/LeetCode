class Solution:
    '''
    只要在数组中找到三个递增的元素即可，不要求这三个元素是否连续，因此，只需维护两个整数变量a, b，用来记录数组中大小递增的前2个元素，满足条件时，应该有：a < b < nums[i]
    '''

    def increasingTriplet(self, nums: List[int]) -> bool:
        m = [float('inf')]*2
        for num in nums:
            if num <= m[0]:
                m[0] = num
            elif num <= m[1]:
                m[1] = num
            else:
                return True
        return False
