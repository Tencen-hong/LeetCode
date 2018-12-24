class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || s.size() < 2)
            return s;
        int interval = numRows - 2;
        string res;
        //find a relationship in (numRows,interval,i,s_pos)
        for (int i = 0; i < numRows; i++) { // row by row
            for (int s_pos = i; s_pos < s.size(); ) {
                res += s[s_pos];//the position that every Column was full ,e.p. PAHN
                s_pos = s_pos + numRows + interval;//the next position that every Column was full
                if (i != 0 && i != numRows - 1) { // deal with zigzap shape
                    if (s_pos - (2 * i) < s.size())
                        res += s[s_pos - (2 * i)]; // the position only 1 character in column
                }
            }
        }

        return res; 
    }
};