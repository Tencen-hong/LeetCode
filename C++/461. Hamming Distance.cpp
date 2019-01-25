class Solution
{
  public:
    int hammingDistance(int x, int y)
    {
        int cnt = 0;
        while (x != 0 || y != 0)
        {
            int a = x & 1;
            int b = y & 1;
            if (a != b)
                cnt++;
            x = x >> 1;
            y = y >> 1;
        }
        return cnt;
    }
};