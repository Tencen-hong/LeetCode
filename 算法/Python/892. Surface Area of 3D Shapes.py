class Solution:
    '''
    表面积=小方块总面积-重叠部分面积
    重叠部分面积 = 左右重叠（重叠2块中，矮的高度*2)  +  上下重叠(2块重叠2面积)  
    '''

    def surfaceArea(self, grid: List[List[int]]) -> int:
        cubes = 0
        overlapping = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cubes += grid[i][j]
                if grid[i][j] >= 2:
                    overlapping += grid[i][j]-1
                if i > 0:
                    overlapping += min(grid[i][j], grid[i-1][j])
                if j > 0:
                    overlapping += min(grid[i][j], grid[i][j-1])
        return cubes*6 - overlapping*2
