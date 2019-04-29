class Solution
{
public:
    bool validateStackSequences(vector<int> &pushed, vector<int> &popped)
    {
        if (pushed.size() != popped.size())
            return false;
        int size = pushed.size();
        stack<int> stk;
        for (int i = 0, j = 0; i < size && j < size; i++)
        {
            stk.push(pushed[i]);
            while (stk.size() > 0 && stk.top() == popped[j])
            {
                stk.pop();
                j++;
            }
        }
        return stk.empty();
    }
};