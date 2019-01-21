class Solution
{
  public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>> &A)
    {
        int m = A.size();
        int n = A[0].size();

        for (int i = 0; i < m; i++)
        {
            reverse(A[i].begin(), A[i].end());
            for (int j = 0; j < n; j++)
            {
                if (A[i][j] == 0)
                    A[i][j] = 1;
                else if (A[i][j] == 1)
                    A[i][j] = 0;
            }
        }
        return A;
    }
};