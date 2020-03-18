class Solution {
public:
    string longestPalindrome(string s) {
        int length = s.size();
        while (length >= 1) {
            //length from n to 1 ，the block with length move from 0 to n
            for (int i = 0; i + length <= s.size(); i++) {
                bool flag = true;
                //determine the boack is palindromic or not
                for (int l = i, r = i + length - 1; l < r; l++, r--) {
                    if (s[l] != s[r]) {
                        flag = false;
                        break;
                    }
                }
                //cause length from long to short ，first is the longest
                if (flag)
                    return s.substr(i, length);
            }

            length--;
        }
        return s;
    }
};