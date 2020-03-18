class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1
            elif i == 0:
                result = max(result, temp)
                temp = 0
        result = max(result, temp)
        return result
