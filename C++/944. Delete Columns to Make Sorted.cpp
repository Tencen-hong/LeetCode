class Solution
{
  public:
    int minDeletionSize(vector<string> &A)
    {
        int m = A.size();
        int n = A[0].size();
        int cnt = 0;
        for (int j = 0; j < n; j++)
        {
            for (int i = 0; i + 1 < m; i++)
            {
                if (A[i + 1][j] < A[i][j])
                {
                    cnt++;
                    break;
                }
            }
        }
        return cnt;
    }
};