class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &T)
    {
        vector<int> ans(T.size());
        stack<int> stk;
        for (int i = 0; i < T.size(); i++)
        {
            while (!stk.empty() && T[i] > T[stk.top()])
            {
                ans[stk.top()] = i - stk.top();
                stk.pop();
            }
            stk.push(i);
        }
        return ans;
    }
};