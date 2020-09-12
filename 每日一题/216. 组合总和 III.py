class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        ans = []

        def dfs(st, en, n, k):
            if len(ans) > k or sum(ans) > n:
                return
            if len(ans) == k and sum(ans) == n:
                ret.append(ans[:])
                return
            for i in range(st, en+1):
                ans.append(i)
                dfs(i+1, en, n, k)
                ans.pop()
        dfs(1, 9, n, k)
        return ret
