class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        //vertical:The skyline viewed from top or bottom;
        //horizontal:The skyline viewed from left or right

        vector<int> vertical(n, 0), horizontal(m, 0);
        // find skyline
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                horizontal[i] = max(horizontal[i], grid[i][j]);
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                vertical[j] = max(vertical[j], grid[i][j]);
            }
        }

        // gridNew:The grid after increasing the height of buildings without affecting skylines
        vector<vector<int>> gridNew = grid;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                gridNew[i][j] = min(vertical[j], horizontal[i]);
            }
        }
        int ans = 0;
        // calculate max increase
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans += gridNew[i][j] - grid[i][j];
            }
        }

        return ans;
    }
};