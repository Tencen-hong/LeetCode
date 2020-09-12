class Solution
{
public:
    vector<vector<int>> ret;
    vector<int> temp;

    int dfs(int start, int end, int k, int n)
    {
        if (temp.size() > k || accumulate(temp.begin(), temp.end(), 0) > n)
        {
            return -1;
        }
        if (temp.size() == k && accumulate(temp.begin(), temp.end(), 0) == n)
        {
            ret.emplace_back(temp);
            return 1;
        }
        for (int x = start; x <= end; x++)
        {
            temp.push_back(x);
            dfs(x + 1, end, k, n);
            temp.pop_back();
        }
        return 0;
    }
    vector<vector<int>> combinationSum3(int k, int n)
    {
        dfs(1, 9, k, n);
        return ret;
    }
};