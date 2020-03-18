class Solution:
    '''
    只需要判断哪个X是战舰头即可，当我们遇到战舰头时，就将总战舰数加一，其余时候都继续遍历。战舰头即战舰的左侧和上侧没有其它的X
    '''

    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (i-1 >= 0 and board[i-1][j] == 'X') or (j-1 >= 0 and board[i][j-1] == 'X'):
                        continue
                    count += 1
        return count
 