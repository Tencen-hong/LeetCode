class Solution
{
public:
    int scoreOfParentheses(string S)
    {
        stack<int> res;
        res.push(0);
        for (auto it : S)
        {
            if (it == '(')
                res.push(0);
            else
            {
                auto v = res.top();
                res.pop();
                auto w = res.top();
                res.pop();
                res.push(w + max(v * 2, 1));
            }
        }
        return res.top();
    }
};