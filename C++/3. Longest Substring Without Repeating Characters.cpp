class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int visit[128];
        fill(visit, visit + 128, -1); //visit[] store the index of s[i]
        int start = 0; // start = the beginning index of temp substring
        int max_str = 0; // max_str = the length of temp substring
        int res = 0;// res = the length of longest substring

        for (int i = 0; i < s.size(); i++) {
            //if duplicate
            if (visit[s[i]] != -1) {
                if (visit[s[i]] >= start ) //only care about the duplicate character after start
                {
                    start = visit[s[i]] + 1;
                    max_str =  i - start ;
                }
            }
            max_str += 1;
            visit[s[i]] = i;
            if (max_str > res)
                res = max_str;
        }

        return res;
    }
};