class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.father = [-1]*20000
        N = len(stones)
        for x, y in stones:
            self.union(x, y+10000)

        return N - len({self.find(x) for x, y in stones})

    def find(self, x):
        return x if self.father[x] == -1 else self.find(self.father[x])

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.father[fx] = fy
