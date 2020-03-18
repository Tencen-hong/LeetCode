class Solution:
    '''
    用一个map存放所有值出现的次数，对于map中的每个num，求出num和num+1出现的次数之和，找出最大值即可
    '''

    def findLHS(self, nums: List[int]) -> int:
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0)+1
        result = 0
        for num, count in nums_count.items():
            if nums_count.get(num+1):
                result = max(result, nums_count.get(num+1) + count)
        return result
