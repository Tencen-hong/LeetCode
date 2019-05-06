class Solution
{
public:
    bool isAlienSorted(vector<string> &words, string order)
    {
        if (words.size() < 2)
            return true;
        for (int i = 0; i < words.size() - 1; i++)
        {
            for (int pos = 0; pos < words[i].size(); pos++)
            {
                if (pos == words.size())
                    return false;
                if (order.find(words[i][pos]) > order.find(words[i + 1][pos]))
                    return false;
                else if (order.find(words[i][pos]) < order.find(words[i + 1][pos]))
                    break;
            }
        }
        return true;
    }
};