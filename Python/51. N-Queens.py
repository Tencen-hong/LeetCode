class Solution:
    '''
    规则：2个queen不能在同一行，同一列，同一对角线
    使用三个helper函数来辅助，使得代码更加清晰，
    1.第一需要DFS函数，一行一行的放置queen，当出现非法的情况时，直接返回上一级 - backtracking的思路
    2.第二个函数就是判断某一点放queen是否合法，因为是一行一行放，所以可以保证不在一行上。
    全局变量cols记录了那一列已经放置了queen，通过检查当前列是否在其中，即可判断是不是同一列有两个queen。
    同时cols的长度也表示已经有多少行放置好了queen，当len(cols) == n的时候可以drawboard并加入result中
同时还有检查对角线，左上右下和左下右上。
    3.第三个函数是根据cols数组画出board，相对简单。比如[2, 4, 1, 3]表示第一行queen在第二列，第二行queen在第四列，第三行queen在第一列，第四行queen在第三列
    '''

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n <= 0:
            return res

        cols = []
        self.dfs(n, cols, res)
        return res

    def dfs(self, n, cols, res):
        if len(cols) == n:
            res.append(self.drawboard(cols))
            return
        for col in range(n):
            if self.isValid(n, cols, col):
                self.dfs(n, cols + [col], res)
            else:
                continue

    def isValid(self, n, cols, col):
        currentRowNumber = len(cols)
        for i in range(currentRowNumber):
            # 同一列出现2个queen  或   同一对角线出现2个queen
            if cols[i] == col or (abs(currentRowNumber - i) == abs(col - cols[i])):
                return False
        return True

    def drawboard(self, cols):
        board = []
        for i in range(len(cols)):
            line = ""
            for j in range(len(cols)):
                if cols[i] == j:
                    line += 'Q'
                else:
                    line += '.'
            board.append(line)
        return board
