class Solution
{
  public:
    bool isToeplitzMatrix(vector<vector<int>> &matrix)
    {
        int m = matrix.size();
        int n = matrix[0].size();
        bool ans = true;
        for (int i = 0; i < m; i++)
        {
            int x = i, y = 0;
            int key = matrix[x][y];
            while (x < m && y < n)
            {
                if (matrix[x][y] != key)
                {
                    ans = false;
                    break;
                }
                x++;
                y++;
            }
        }

        for (int j = 1; j < n; j++)
        {
            int x = 0, y = j;
            int key = matrix[x][y];
            while (x < m && y < n)
            {
                if (matrix[x][y] != key)
                {
                    ans = false;
                    break;
                }
                x++;
                y++;
            }
        }

        return ans;
    }
};