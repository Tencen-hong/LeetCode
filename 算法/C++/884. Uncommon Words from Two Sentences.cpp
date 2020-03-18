class Solution
{
public:
    vector<string> uncommonFromSentences(string A, string B)
    {
        vector<string> ans;
        map<string, int> myMap;
        A.push_back(' ');
        B.push_back(' ');
        string word;
        for (int i = 0; i < A.size(); ++i)
        {
            if (A[i] == ' ')
            {
                myMap[word]++;
                word = "";
            }
            else
            {
                word += A[i];
            }
        }
        word = "";
        for (int i = 0; i < B.size(); ++i)
        {
            if (B[i] == ' ')
            {
                myMap[word]++;
                word = "";
            }
            else
            {
                word += B[i];
            }
        }
        for (auto &item : myMap)
        {
            if (item.second == 1)
            {
                ans.push_back(item.first);
            }
        }
        return ans;
    }
};