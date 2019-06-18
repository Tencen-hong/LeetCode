class Solution:
    '''
    对v排序，i找到第一个和排序后的数组v不相等的元素，j找到最后一个和排序后的数组v不相等的元素，如果i<=j说明存在这样一个长度，长度为j-i+1，否则不存在这样一个长度，则返回0～
    '''

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        v = sorted(nums)
        i, j = 0, len(nums)-1
        while i < len(nums) and nums[i] == v[i]:
            i += 1
        while j >= 0 and nums[j] == v[j]:
            j -= 1
        return j-i+1 if i <= j else 0
