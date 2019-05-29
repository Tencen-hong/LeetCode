class Solution:
    def numSquares(self, n: int) -> int:
        q1 = [0]
        q2 = []
        level = 0
        visited = [False]*(n+1)
        while True:
            level += 1
            for v in q1:
                i = 0
                while True:
                    i += 1
                    t = v+i*i
                    if t == n:
                        return level
                    elif t > n:
                        break
                    if visited[t]:
                        continue
                    q2.append(t)
                    visited[t] = True
            q1 = q2
            q2 = []
        return 0
