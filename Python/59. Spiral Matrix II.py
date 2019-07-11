class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        layers = (n-1)//2
        x, y, num = 0, 0, 1
        for l in range(layers+1):
            while y < n-l:
                res[x][y] = num
                num += 1
                y += 1
            y -= 1
            x += 1
            while x < n-l:
                res[x][y] = num
                num += 1
                x += 1
            x -= 1
            y -= 1
            while y >= l:
                res[x][y] = num
                num += 1
                y -= 1
            y += 1
            x -= 1
            while x > l:
                res[x][y] = num
                num += 1
                x -= 1
            x += 1
            y += 1
        return res
