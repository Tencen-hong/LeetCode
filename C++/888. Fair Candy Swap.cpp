class Solution
{
public:
    vector<int> fairCandySwap(vector<int> &A, vector<int> &B)
    {
        int diff = (accumulate(A.begin(), A.end(), 0) - accumulate(B.begin(), B.end(), 0)) / 2;
        unordered_set<int> S(A.begin(), A.end());
        for (int i = 0; i < B.size(); i++)
        {
            if (S.count(diff + B[i]))
                return {B[i] + diff, B[i]};
        }
        return {0, 0};
    }
};