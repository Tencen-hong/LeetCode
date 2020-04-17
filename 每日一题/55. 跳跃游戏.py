class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_right = 0
        for i in range(n):
            if i > max_right:
                return False
            max_right = max(max_right, i+nums[i])

        return True
