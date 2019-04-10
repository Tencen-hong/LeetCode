class Solution
{
  public:
    int _order[128] = {0};
    string customSortString(string S, string T)
    {
        for (int i = 0; i < S.size(); i++)
        {
            _order[S[i]] = i + 1;
        }
        sort(T.begin(), T.end(),
             [&](char &a, char &b) {
                 return _order[a] < _order[b];
             });
        return T;
    }
};