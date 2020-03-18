class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res, visit = 0, [0]*len(nums)
        for num in nums:
            count, x = 0, num
            while not visit[x]:
                visit[x], count, x = 1, count+1, nums[x]
                res = max(res, count)
        return res
