class Solution
{
public:
    int largestPerimeter(vector<int> &A)
    {
        sort(A.begin(), A.end());
        int r = A.size() - 1, l = r - 2;
        int res = 0;
        while (l >= 0)
        {
            if (A[l] + A[l + 1] > A[r])
            {
                res += A[l] + A[l + 1] + A[r];
                break;
            }
            r--;
            l = r - 2;
        }
        return res;
    }
};