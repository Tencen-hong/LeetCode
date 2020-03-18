class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        // if board[i][j]==0 and its value should be changed, set board[i][j]=2;
        // if board[i][j]==1 and its value should be changed, set board[i][j]=3;
        int m = board.size();
        int n = board[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int cnt = 0;
                if (i - 1 >= 0) {
                    cnt += board[i - 1][j] & 1;
                    if (j - 1 >= 0)
                        cnt += board[i - 1][j - 1] & 1;
                    if (j + 1 < n)
                        cnt += board[i - 1][j + 1] & 1;

                }
                if (i + 1 < m) {
                    cnt += board[i + 1][j] & 1;
                    if (j - 1 >= 0)
                        cnt += board[i + 1][j - 1] & 1;
                    if (j + 1 < n)
                        cnt += board[i + 1][j + 1] & 1;
                }
                if (j - 1 >= 0)
                    cnt += board[i][j - 1] & 1;
                if (j + 1 < n)
                    cnt += board[i][j + 1] & 1;

                if (board[i][j] == 1) {
                    if (cnt < 2 || cnt > 3)
                        board[i][j] = 3;
                }
                else if (board[i][j] == 0) {
                    if (cnt == 3)
                        board[i][j] = 2;
                }

            }
        }
        //update
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 2)
                    board[i][j] = 1;
                else if (board[i][j] == 3)
                    board[i][j] = 0;

            }
        }


    }
};