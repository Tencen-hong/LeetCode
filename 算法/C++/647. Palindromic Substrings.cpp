class Solution
{
public:
    int countSubstrings(string s)
    {
        if (s.size() == 0)
            return 0;
        int res = 0;
        for (int i = 0; i < s.size(); i++)
        {
            res += extendPalindrom(s, i, i);
            res += extendPalindrom(s, i, i + 1);
        }
        return res;
    }
    int extendPalindrom(string s, int left, int right)
    {
        int cnt = 0;
        while (left >= 0 && right < s.size() && s[left] == s[right])
        {
            cnt++;
            left--;
            right++;
        }
        return cnt;
    }
};