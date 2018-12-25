class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) // if strs is empty
            return "";
        string prefix = strs[0];
        for (int i = 1; i < strs.size(); i++) {
            if (strs[i].size() < prefix.size()) // make prefix be the shortest one
                prefix = strs[i];
        }

        for (int i = 0; i < strs.size(); i++) {
            for (int j = 0; j < prefix.size(); j++) {
                if (prefix[j] != strs[i][j])
                    prefix =  prefix.substr(0, j); // cut off the  uncommon prefix
            }
        }
        return prefix;
    }
};