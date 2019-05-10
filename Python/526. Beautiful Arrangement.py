class Solution:
    def countArrangement(self, N: int) -> int:
        self.visited = [False]*(N+1)
        self.count = 0
        self.N = N

        def dfs(index):
            if index == self.N+1:
                self.count += 1
                return
            for i in range(1, self.N+1):
                if self.visited[i] == False and (i % index == 0 or index % i == 0):
                    self.visited[i] = True
                    dfs(index+1)
                    self.visited[i] = False
        dfs(1)
        return self.count
