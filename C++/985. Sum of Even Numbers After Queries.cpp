class Solution
{
  public:
    int getEvensum(vector<int> A)
    {
        int sum = 0;
        for (int i = 0; i < A.size(); i++)
        {
            if (A[i] % 2 == 0)
            {
                sum += A[i];
            }
        }
        return sum;
    }

    vector<int> sumEvenAfterQueries(vector<int> &A, vector<vector<int>> &queries)
    {
        vector<int> ans;
        int even_sum = getEvensum(A);
        for (int i = 0; i < queries.size(); i++)
        {
            int index = queries[i][1];
            int val = queries[i][0];
            if (A[index] % 2 == 0)
            {
                even_sum -= A[index];
            }
            A[index] += val;
            if (A[index] % 2 == 0)
            {
                even_sum += A[index];
            }
            ans.push_back(even_sum);
        }
        return ans;
    }
};