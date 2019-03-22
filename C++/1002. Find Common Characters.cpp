class Solution
{
  public:
    vector<string> commonChars(vector<string> &A)
    {
        vector<string> ans;
        const int N = A.size();
        int count_[N][128] = {0};//统计各字符串字母频率表
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < A[i].size(); j++)
            {
                count_[i][A[i][j]]++;
            }
        }

        for (int j = 'a'; j <= 'z'; j++)
        {
            int min_occurance = INT_MAX;//公共字母重复次数取出现频率最低的
            for (int i = 0; i < N; i++)
            {
                if (min_occurance > count_[i][j])
                {
                    min_occurance = count_[i][j];
                }
            }

            char c = j;
            string str;
            stringstream stream;
            stream << c;
            str = stream.str();
            for (int k = 0; k < min_occurance; k++)
            {
                ans.push_back(str);
            }
        }

        return ans;
    }
};