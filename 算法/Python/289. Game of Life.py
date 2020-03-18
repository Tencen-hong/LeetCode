class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # if board[i][j]==0 and its value should be changed, set board[i][j]=2;
        # if board[i][j]==1 and its value should be changed, set board[i][j]=3;

        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                n = 0
                if i-1 >= 0:
                    n += board[i-1][j] % 2
                    if j-1 >= 0:
                        n += board[i-1][j-1] % 2
                    if j+1 < col:
                        n += board[i-1][j+1] % 2
                if i+1 < row:
                    n += board[i+1][j] % 2
                    if j-1 >= 0:
                        n += board[i+1][j-1] % 2
                    if j+1 < col:
                        n += board[i+1][j+1] % 2
                if j-1 >= 0:
                    n += board[i][j-1] % 2
                if j+1 < col:
                    n += board[i][j+1] % 2

                if board[i][j] == 1:
                    if n < 2 or n > 3:
                        board[i][j] = 3
                elif board[i][j] == 0:
                    if n == 3:
                        board[i][j] = 2

        # update
        for i in range(row):
            for j in range(col):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
