class Solution
{
  public:
    /*
    When s []= i, start marking at 0, and when s []= d, start marking at n.
    */
    vector<int> diStringMatch(string S)
    {
        int N = S.size();
        int i = 0, j = N;
        vector<int> ans;
        for (int k = 0; k < S.size(); k++)
        {
            if (S[k] == 'I')
            {
                ans.push_back(i);
                i += 1;
            }
            else if (S[k] == 'D')
            {
                ans.push_back(j);
                j -= 1;
            }
        }
        ans.push_back(i);
        return ans;
    }
};