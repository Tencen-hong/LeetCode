class Solution:
    '''
    按序读入moves, A为1, B为-1,
    每走一步，检查游戏是否有胜利者：
        -每行棋子相同
        -每列棋子相同
        -对角线棋子相同
        返回相同的棋子 或 0
    未产生胜利者，若棋盘没有铺满：
        返回 Pending
        否则返回 Draw
    '''

    def tictactoe(self, moves: List[List[int]]) -> str:
        x = 1
        a = [[0 for i in range(3)] for j in range(3)]
        for move in moves:
            a[move[0]][move[1]] = x
            y = self.check(a)
            if y == 1:
                return "A"
            elif y == -1:
                return "B"
            x = -x

        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"

    def check(self, a):
        for i in range(3):
            if a[i][0] == a[i][1] == a[i][2]:
                return a[i][0]
        for j in range(3):
            if a[0][j] == a[1][j] == a[2][j]:
                return a[0][j]
        if a[0][0] == a[1][1] == a[2][2]:
            return a[0][0]
        if a[0][2] == a[1][1] == a[2][0]:
            return a[0][2]
        return 0
