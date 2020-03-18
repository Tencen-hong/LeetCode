class Solution
{
public:
    vector<string> res;
    void help(string s, int index)
    {
        if (index == s.size())
        {
            res.push_back(s);
            return;
        }
        help(s, index + 1);
        if (isalpha(s[index]))
        {
            s[index] ^= 32;
            help(s, index + 1);
        }
    }
    vector<string> letterCasePermutation(string S)
    {

        help(S, 0);
        return res;
    }
};