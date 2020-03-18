class Solution
{
  public:
    int uniqueMorseRepresentations(vector<string> &words)
    {
        set<string> ans;
        string alphabet[] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
        for (int i = 0; i < words.size(); i++)
        {
            string temp;
            for (int j = 0; j < words[i].size(); j++)
            {
                temp += alphabet[words[i][j] - 'a'];
            }
            ans.insert(temp);
        }
        return ans.size();
    }
};