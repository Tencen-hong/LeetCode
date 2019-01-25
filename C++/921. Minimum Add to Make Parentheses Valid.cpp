class Solution
{
  public:
    int minAddToMakeValid(string S)
    {
        stack<char> _stack;
        int ans = 0;
        for (int i = 0; i < S.size(); i++)
        {
            if (S[i] == '(')
            {
                _stack.push(S[i]);
            }
            else if (S[i] == ')')
            {
                if (_stack.empty())
                    ans++;
                else
                    _stack.pop();
            }
        }
        ans += _stack.size();
        return ans;
    }
};