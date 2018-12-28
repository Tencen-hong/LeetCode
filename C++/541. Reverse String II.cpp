class Solution {
public:
    string reverseStr(string s, int k) {

        for (int i = 0; i < s.size(); i += 2 * k) {
            int l = i;
            int r = i + k - 1;
            while (r >= s.size()) r--;
            while (l < r)
                swap(s[l++], s[r--]);
        }
        return s;
    }
};