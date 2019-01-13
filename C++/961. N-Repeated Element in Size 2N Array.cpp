class Solution
{
  public:
    int repeatedNTimes(vector<int> &A)
    {
        set<int> mymap;
        for (int i = 0; i < A.size(); i++)
        {
            if (mymap.count(A[i]) == 1)
                return A[i];
            else
                mymap.insert(A[i]);
        }
        return NULL;
    }
};