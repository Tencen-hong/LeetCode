class Solution
{
  public:
    void flipp_row(vector<int> &vec)
    {
        for (int i = 0; i < vec.size(); i++)
        {
            if (vec[i] == 0)
                vec[i] = 1;
            else
                vec[i] = 0;
        }
    }
    void flipp_col(vector<vector<int>> &A, int col_number)
    {
        for (int i = 0; i < A.size(); i++)
        {
            if (A[i][col_number] == 0)
                A[i][col_number] = 1;
            else
                A[i][col_number] = 0;
        }
    }
    int matrixScore(vector<vector<int>> &A)
    {
        // 按行翻转将第一列全部转成1，后面每一列1的个数小于0的个数时，按列翻转
        int m = A.size();
        int n = A[0].size();
        for (int i = 0; i < m; i++)
        {
            if (A[i][0] == 0)
                flipp_row(A[i]);
        }
        for (int j = 1; j < n; j++)
        {
            int cnt = 0;
            for (int i = 0; i < m; i++)
            {
                if (A[i][j] == 1)
                {
                    cnt++;
                }
            }
            if (cnt <= m / 2)
            {
                flipp_col(A, j);
            }
        }

        int ans = 0;
        for (int i = 0; i < m; i++)
        {
            int k = 0;
            for (int j = n - 1; j >= 0; j--)
            {
                ans += A[i][j] * pow(2, k++);
            }
        }
        return ans;
    }
};