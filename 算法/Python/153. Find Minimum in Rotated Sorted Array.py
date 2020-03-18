class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return nums
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            l, r = (m+1, r) if nums[m] > nums[r] else (l, m)
        return nums[l]
