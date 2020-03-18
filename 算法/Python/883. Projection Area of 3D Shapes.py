class Solution:
    '''
    1.俯视图：矩阵中非0元素个数
    2.正视图：矩阵中每行最大的元素的和
    3.侧视图：矩阵中每列最大的元素的和
    '''

    def projectionArea(self, grid: List[List[int]]) -> int:

        top_view = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    top_view += 1
        front_view = 0

        for i in range(len(grid)):
            front_view += max(grid[i])

        side_view = 0
        for j in range(len(grid[0])):
            side_view += max([grid[i][j] for i in range(len(grid))])

        result = top_view+front_view+side_view
        return result
