class Solution {
public:

    int romanToInt(string s) {
        //define roman as integer
        int table[128] = {0};
        table['I'] = 1;
        table['V'] = 5;
        table['X'] = 10;
        table['L'] = 50;
        table['C'] = 100;
        table['D'] = 500;
        table['M'] = 1000;

        // if s.size()<=1
        if (s.size() == 0)
            return 0;
        if (s.size() == 1)
            return table[s[0]];

        int temp = 0;
        int res = 0;
        for (int i = 0; i < s.size();) {
            // the roman_before < roman-after like IV=4
            if (i + 1 < s.size() && table[s[i]] < table[s[i + 1]]) {
                temp = table[s[i + 1]] - table[s[i]];
                i += 2;
            } else { //normal
                temp = table[s[i]];
                i++;
            }
            res += temp;
        }
        return res;
    }
};