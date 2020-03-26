class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        total_surface = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] > 0:
                    total_surface += self.calculate(grid, i, j)
                # print(total_surface)

        return total_surface

    def calculate(self, grid, i, j):
        cross_surface = 0
        if i-1 >= 0:
            cross_surface += min(grid[i][j], grid[i-1][j])
        if i+1 < len(grid):
            cross_surface += min(grid[i][j], grid[i+1][j])
        if j-1 >= 0:
            cross_surface += min(grid[i][j], grid[i][j-1])
        if j+1 < len(grid[i]):
            cross_surface += min(grid[i][j], grid[i][j+1])

        return grid[i][j] * 4 - cross_surface + 2
