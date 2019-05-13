class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        N = len(M)
        visited = [False]*N

        def dfs(student):
            visited[student] = True
            for classmate in range(N):
                if classmate != student and M[student][classmate] and not visited[classmate]:
                    dfs(classmate)
        circles = 0
        for i in range(N):
            if visited[i] == False:
                dfs(i)
                circles += 1
        return circles
