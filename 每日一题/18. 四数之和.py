class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                while right > left:
                    t_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if t_sum == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif t_sum < target:
                        left += 1
                    elif t_sum > target:
                        right -= 1
        ret = []
        for it in ans:
            ret.append(list(it))
        return ret
