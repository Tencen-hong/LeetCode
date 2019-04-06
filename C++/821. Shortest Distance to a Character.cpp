class Solution
{
  public:
    vector<int> shortestToChar(string S, char C)
    {
        vector<int> ans;
        for (int i = 0; i < S.size(); ++i)
        {
            int left = S.rfind(C, i);
            int right = S.find(C, i);
            int temp;
            if (left == -1)
            {
                temp = abs(right - i);
            }
            else if (right == -1)
            {
                temp = abs(left - i);
            }
            else
            {
                temp = min(abs(left - i), abs(right - i));
            }
            ans.push_back(temp);
        }
        return ans;
    }
};