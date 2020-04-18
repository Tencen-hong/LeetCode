class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = []
        while left <= right:
            water = (right - left) * min(height[left], height[right])
            res.append(water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max(res)
