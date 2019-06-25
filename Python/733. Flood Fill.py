class Solution:
    '''
        1.保存起点的像素值
        2.从起点开始向四周扩散，符合条件(像素值=起点像素值，与上一个符合的坐标点直接连接)的坐标的像素值设为新像素值
    '''

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        visited = [[False for j in range(len(image[0]))]
                   for i in range(len(image))]

        def bfs(i, j):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
                return
            if visited[i][j]:
                return
            image[i][j] = newColor
            visited[i][j] = True
            # dp
            if i-1 >= 0 and image[i-1][j] == oldColor:
                bfs(i-1, j)
            # down
            if i+1 < len(image) and image[i+1][j] == oldColor:
                bfs(i+1, j)
            # left
            if j-1 >= 0 and image[i][j-1] == oldColor:
                bfs(i, j-1)
            # right
            if j+1 < len(image[0]) and image[i][j+1] == oldColor:
                bfs(i, j+1)

        bfs(sr, sc)
        return image
