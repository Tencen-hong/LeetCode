class Solution
{
  public:
    string reverseWords(string s)
    {
        s.push_back(' ');
        int end = s.find(' ');
        int start = 0;
        while (end != s.npos)
        {
            reverse(s.begin() + start, s.begin() + end);
            start = end + 1;
            end = s.find(' ', start);
        }
        s.pop_back();
        return s;
    }
};