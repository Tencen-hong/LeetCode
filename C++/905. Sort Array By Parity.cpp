class Solution
{
  public:
    vector<int> sortArrayByParity(vector<int> &A)
    {
        int i = 0, j = A.size() - 1;
        while (i < j)
        {
            while (A[i] % 2 == 0)
                i++;
            while (A[j] % 2 == 1)
                j--;
            if (i < j)
                swap(A[i], A[j]);
        }
        return A;
    }
};