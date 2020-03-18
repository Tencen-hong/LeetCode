class Solution
{
public:
    string frequencySort(string s)
    {
        unordered_map<char, int> freq;
        vector<string> decrease(s.size() + 1, "");
        for (auto it : s)
            freq[it]++;
        for (auto it : freq)
        {
            char ch = it.first;
            int count = it.second;
            decrease[count].append(count, ch);
        }
        string res;
        for (int i = decrease.size() - 1; i >= 0; i--)
        {
            if (decrease[i] != "")
            {
                res.append(decrease[i]);
            }
        }
        return res;
    }
};