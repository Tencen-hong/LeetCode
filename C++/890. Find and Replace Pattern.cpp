class Solution
{
  public:
    vector<string> findAndReplacePattern(vector<string> &words, string pattern)
    {
        vector<string> ans;
        //Character-by-character comparison for each string
        for (int i = 0; i < words.size(); i++)
        {
            map<char, char> _map;      //Pattern and word mapping
            bool flag = true;          // does it reach the requirement
            bool visit[128] = {false}; //Mark the characters that have appeared in the words string
            for (int j = 0; j < pattern.size(); j++)
            {
                if (_map.find(pattern[j]) == _map.end())
                {                                    //Mappings that do not appear in the pattern
                    if (visit[words[i][j]] == false) //At the same time, it has not appeared in words.
                    {
                        _map[pattern[j]] = words[i][j]; //Record mapping
                        visit[words[i][j]] = true;
                    }
                    else
                    { //Has appeared in words (has already recorded mapping)
                        flag = false;
                        break;
                    }
                }
                else if (_map[pattern[j]] != words[i][j])
                { //After checking the mapping table, it is inconsistent with the previous mapping relationship.
                    flag = false;
                    break;
                }
                else if (_map[pattern[j]] == words[i][j])
                {
                    continue;
                }
            }
            if (flag)
                ans.push_back(words[i]);
        }
        return ans;
    }
};