class Solution:
    '''
    1.将与边界连接的'O'修改成'A'
    2.将内部的'O'修改成'X'
    3.将'A'还原成'O'
    '''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        H = len(board)
        if H == 0:
            return
        W = len(board[0])

        def change(i, j):
            if i < 0 or j < 0 or i >= H or j >= W or board[i][j] != 'O':
                return
            if board[i][j] == 'O':
                board[i][j] = 'A'
                change(i+1, j)
                change(i-1, j)
                change(i, j+1)
                change(i, j-1)

        for i in range(H):
            change(i, 0)
            change(i, W-1)
        for j in range(W):
            change(0, j)
            change(H-1, j)

        for i in range(H):
            for j in range(W):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
