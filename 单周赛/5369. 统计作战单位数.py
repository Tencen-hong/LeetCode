class Solution:
    def numTeams(self, rating: List[int]) -> int:
        self.res = []
        self.dfs(rating, 0, [])
        self.dfs(rating[::-1], 0, [])
        return len(self.res)

    def dfs(self, rating, idx, unit):
        if len(unit) == 3:
            self.res.append(unit[:])
            return
        for j in range(idx, len(rating)):
            if not unit or unit[-1] < rating[j]:
                unit.append(rating[j])
                self.dfs(rating, j, unit)
                unit.pop()
