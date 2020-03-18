class Solution
{
public:
    int minFallingPathSum(vector<vector<int>> &A)
    {
        vector<vector<int>> dp = A;
        for (int i = 1; i < A.size(); i++)
        {
            for (int j = 0; j < A.size(); j++)
            {
                if (j == 0)
                {
                    dp[i][j] = A[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1]);
                }
                else if (j == A.size() - 1)
                {
                    dp[i][j] = A[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1]);
                }
                else
                {
                    dp[i][j] = A[i][j] + min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i - 1][j + 1]));
                }
            }
        }
        return *min_element(dp[A.size() - 1].begin(), dp[A.size() - 1].end());
    }
};