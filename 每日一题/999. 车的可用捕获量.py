class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x = y = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    x = i
                    y = j
                    break
        res = 0
        for i in range(x, -1, -1):
            if board[i][y] == 'p':
                res += 1
                break
            elif board[i][y] == 'B':
                break
        for i in range(x, len(board)):
            if board[i][y] == 'p':
                res += 1
                break
            elif board[i][y] == 'B':
                break
        for j in range(y, -1, -1):
            if board[x][j] == 'p':
                res += 1
                break
            elif board[x][j] == 'B':
                break
        for j in range(y, len(board[x])):
            if board[x][j] == 'p':
                res += 1
                break
            elif board[x][j] == 'B':
                break
        return res
