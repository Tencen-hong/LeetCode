class Solution:
    '''
     DFS+回溯
    '''

    def exist(self, board: List[List[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])
        visited=[[False for j in range(col)] for i in range(row)]
        
        def dfs(board,word,index,i,j):
            if index==len(word):
                return True
            if (i<0) or (j<0) or (i>=row) or (j>=col):
                return False
            if visited[i][j]:
                return False
            if board[i][j]!=word[index]:
                return False
            visited[i][j]=True
            res = dfs(board,word,index+1,i-1,j) or dfs(board,word,index+1,i+1,j) or dfs(board,word,index+1,i,j-1) or dfs(board,word,index+1,i,j+1)
            visited[i][j]=False
            return res
        for i in range(row):
            for j in range(col):
                if dfs(board,word,0,i,j):
                    return True
        return False
