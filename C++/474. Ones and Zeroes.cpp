class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        //dp problem,针对每一个字符串，实质上我们都采取两种策略，选这个字符串，还是不选。做决定之前，先统计这个字符串(第i个)有多少个0与1，分别记为m0与n0，如果不选这个字符串，那么dp[m][n]的值不会发生任何改变，但是选了之后，它的值就是用了m-m0个0 与n-n0个1，所得到的最多的字符串，也就是f[m-m0][n-n0]再加上1
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (auto &it : strs) {
            int ones = 0;
            int zeroes = 0;
            for (int i = 0; i < it.size(); i++) {
                if (it[i] == '1')
                    ones++;
                else if (it[i] == '0')
                    zeroes++;
            }

            for (int j = m; j >= zeroes; j--) {
                for (int k = n; k >= ones; k--) {
                    dp[j][k] = max(dp[j][k], dp[j - zeroes][k - ones] + 1);
                }
            }

        }

        return dp[m][n];
    }
};