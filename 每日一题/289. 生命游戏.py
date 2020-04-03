class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # -1 表示本来是活得，更新后转成死的
        # 2 表示本来是死的，更新后转成活的
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.changeState(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

        print(board)
    def changeState(self, board, x, y):
        alive = 0
        dead = 0
        for i in (x-1, x, x+1):
            for j in (y-1, y, y+1):
                if i < 0 or i >= len(board):
                    continue
                if j < 0 or j >= len(board[i]):
                    continue
                if i == x and j == y:
                    continue
                if board[i][j] == 0 or board[i][j] == 2:  # 已经死和 活转成死
                    dead += 1
                elif board[i][j] == 1 or board[i][j] == -1:  # 已经活和 死转成活
                    alive += 1

        if alive < 2:
            if board[x][y] == 1:
                board[x][y] = -1
        elif alive > 3:
            if board[x][y] == 1:
                board[x][y] = -1
        elif alive == 3:
            if board[x][y] == 0:
                board[x][y] = 2
