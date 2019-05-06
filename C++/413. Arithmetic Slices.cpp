class Solution
{
public:
    int numberOfArithmeticSlices(vector<int> &A)
    {
        int res = 0, count = 1;
        if (A.size() < 3)
            return 0;
        for (int i = 1; i < A.size() - 1; i++)
        {
            if (A[i + 1] - A[i] == A[i] - A[i - 1])
            {
                res += count++; //arithmetic增加的个数符合等差数列
            }
            else
            {
                count = 1;
            }
        }
        return res;
    }
};