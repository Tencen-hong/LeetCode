class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []

        def dfs(nums, res, tmp, k):
            if len(tmp) >= 2:
                res.append(tmp[:])
            for i in range(k, len(nums)):
                if len(tmp) == 0 or nums[i] >= tmp[-1]:
                    tmp.append(nums[i])
                    dfs(nums, res, tmp, i+1)
                    tmp.pop()

        dfs(nums, res, tmp, 0)

        res = list(set([tuple(t) for t in res]))
        res = [list(v) for v in res]

        return res
