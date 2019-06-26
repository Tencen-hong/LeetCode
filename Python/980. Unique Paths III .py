class Solution:
    '''
    1.遍历矩阵，记录起始和终止位置，以及值为0的位置
    2.从起始位置开始，做dfs，走到终点并且经历所有0值点则为合理路径
    '''

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start, end = (), ()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] == 0:
                    visited.add((i, j))
        self.ret = 0
        visited.add(start)

        def dfs(start, end, visited_copy):
            if start == end and not visited_copy:
                self.ret += 1
                return
            if start not in visited_copy:
                return
            else:
                visited_copy.remove(start)

            i = start[0]
            j = start[1]
            if i > 0:
                dfs((i-1, j), end, visited_copy.copy())
            if i+1 < len(grid):
                dfs((i+1, j), end, visited_copy.copy())
            if j > 0:
                dfs((i, j-1), end, visited_copy.copy())
            if j+1 < len(grid[0]):
                dfs((i, j+1), end, visited_copy.copy())

        dfs(start, end, visited.copy())
        return self.ret
