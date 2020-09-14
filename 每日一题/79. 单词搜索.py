class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            result = False
            visited.add((i, j))
            for di, dj in directions:
                newi, newj = i+di, j+dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k+1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        visited = set()
        h = len(board)
        w = len(board[0])
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        return False
