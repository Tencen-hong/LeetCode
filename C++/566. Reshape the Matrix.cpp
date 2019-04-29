class Solution
{
public:
    vector<vector<int>> matrixReshape(vector<vector<int>> &nums, int r, int c)
    {
        int m = nums.size();
        int n = nums[0].size();
        if (m * n != r * c)
        {
            return nums;
        }
        vector<vector<int>> res;
        int x = 0, y = 0;
        for (int i = 0; i < r; i++)
        {
            vector<int> temp(c);
            for (int j = 0; j < c; j++)
            {
                if (y >= n)
                {
                    y = 0;
                    x++;
                }
                temp[j] = nums[x][y++];
            }
            res.push_back(temp);
        }
        return res;
    }
};