class Solution
{
  public:
    vector<int> f; //保存x的上级节点
    int count;     //统计区域数量
    int n;         //变长
    int g(int x, int y, int k)
    {
        return (x * n + y) * 4 + k;
    }
    int find(int x)
    {
        while (x != f[x])
        {
            x = f[x];
        }
        return x;
    }
    void _union(int x, int y)
    {
        int fx = find(x);
        int fy = find(y);
        if (fx != fy)
        {
            f[fx] = fy;
            count--;
        }
    }
    int regionsBySlashes(vector<string> &grid)
    {
        n = grid.size();
        count = 4 * n * n;
        f.resize(4 * n * n);
        for (int i = 0; i < 4 * n * n; i++)
        {
            f[i] = i;
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i > 0)
                {
                    _union(g(i - 1, j, 2), g(i, j, 0));
                }
                if (j > 0)
                {
                    _union(g(i, j - 1, 1), g(i, j, 3));
                }
                if (grid[i][j] != '\\')
                {
                    _union(g(i, j, 0), g(i, j, 3));
                    _union(g(i, j, 1), g(i, j, 2));
                }
                if (grid[i][j] != '/')
                {
                    _union(g(i, j, 0), g(i, j, 1));
                    _union(g(i, j, 2), g(i, j, 3));
                }
            }
        }
        return count;
    }
};