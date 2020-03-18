class Solution
{
  public:
    int calculate_perimeter(vector<vector<int>> &grid, int x, int y)
    {
        int perimeter = 4;
        //up
        if (grid[x][y - 1] == 1)
            perimeter--;
        //down
        if (grid[x][y + 1] == 1)
            perimeter--;
        //left
        if (grid[x - 1][y] == 1)
            perimeter--;
        //right
        if (grid[x + 1][y] == 1)
            perimeter--;
        return perimeter;
    }
    int islandPerimeter(vector<vector<int>> &grid)
    {
        int ans = 0;
        int m = grid.size();
        int n = grid[0].size();
        grid.insert(grid.begin(), vector<int>(n, 0));
        grid.push_back(vector<int>(n, 0));
        for (int i = 0; i < grid.size(); i++)
        {
            grid[i].insert(grid[i].begin(), 0);
            grid[i].push_back(0);
        }
        for (int i = 1; i < grid.size() - 1; i++)
        {
            for (int j = 1; j < grid[0].size() - 1; j++)
            {
                if (grid[i][j] == 1)
                {
                    ans += calculate_perimeter(grid, i, j);
                }
            }
        }

        return ans;
    }
};