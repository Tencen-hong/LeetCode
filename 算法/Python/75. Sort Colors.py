class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, blue = 0, len(nums)-1
        i = 0
        while i <= blue:
            if nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            elif nums[i] == 0 and red < i:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
            else:
                i += 1
