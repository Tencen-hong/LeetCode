class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        start = 0
        product = 1
        for end in range(len(nums)):
            product *= nums[end]
            while start <= end and product >= k:
                product /= nums[start]
                start += 1
            res += end - start + 1
        return res
