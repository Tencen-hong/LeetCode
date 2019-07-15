class Solution:
    '''
    初始对角线方向为右上方（偏移量：行-1, 列+1），遇到边界时转向左下方（偏移量：行+1, 列-1）
对于边界的处理：
    向右上方移动遇到上边界时，若未达到右边界，则向右移动（偏移量：行+0，列+1），否则向下移动（偏移量：行+1，列+0）
    向左下方移动遇到左边界时，若未达到下边界，则向下移动（偏移量：行+1，列+0），否则向右移动（偏移量：行+0，列+1）
    '''

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        row, col = len(matrix), len(matrix[0])
        i, j, k = 0, 0, 1
        res = []
        for d in range(row * col):
            res.append(matrix[i][j])
            if k > 0:
                di, dj = i - 1, j + 1
            else:
                di, dj = i + 1, j - 1
            if 0 <= di < row and 0 <= dj < col:
                i, j = di, dj
            else:
                if k > 0:
                    if j + 1 < col:
                        j += 1
                    else:
                        i += 1
                else:
                    if i + 1 < row:
                        i += 1
                    else:
                        j += 1
                k *= -1

        return res
