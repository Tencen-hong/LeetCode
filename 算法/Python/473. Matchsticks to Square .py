class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 4:
            return False
        _sum = sum(nums)
        div, mod = divmod(_sum, 4)
        if mod != 0 or max(nums) > _sum / 4:
            return False
        nums.sort(reverse=True)
        target = [div] * 4
        return self.dfs(nums, 0, target)

    def dfs(self, nums, index, target):
        if index == len(nums):
            return True
        num = nums[index]
        for i in range(4):
            if target[i] >= num:
                target[i] -= num
                if self.dfs(nums, index + 1, target):
                    return True
                target[i] += num
        return False
