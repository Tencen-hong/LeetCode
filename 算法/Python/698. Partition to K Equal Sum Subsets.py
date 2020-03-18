class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(nums, k, start, curSum, target, visited, numbers):
            if curSum > target:
                return False
            if k == 0 and numbers == len(nums):  # 找齐了k个子集 并且所有数字都使用了
                return True
            if curSum == target:  # 找到了一个子集
                return dfs(nums, k - 1, 0, 0, target, visited, numbers)
            for i in range(start, len(nums)):
                if visited[i] is False:
                    visited[i] = True
                    if dfs(nums, k, i+1, curSum+nums[i], target, visited, numbers+1):
                        return True
                    visited[i] = False
            return False

        if k == 1:
            return True
        if k > len(nums):
            return False
        if sum(nums) % k != 0:
            return False
        visited = [False] * len(nums)
        return dfs(nums, k, 0, 0, sum(nums)//k, visited, 0)
