class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board)

    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        board[i][j] = str(k)
                        if self.isValid(board, i, j) and self.dfs(board):
                            return True
                        else:
                            board[i][j] = '.'
                    return False

        return True

    def isValid(self, board, row, col):
        for i in range(9):
            if i != row and board[i][col] == board[row][col]:
                return False

        for j in range(9):
            if j != col and board[row][j] == board[row][col]:
                return False

        start_x = row//3 * 3
        start_y = col//3 * 3
        for i in range(start_x, start_x+3):
            for j in range(start_y, start_y+3):
                if i != row and j != col and board[i][j] == board[row][col]:
                    return False
        return True
