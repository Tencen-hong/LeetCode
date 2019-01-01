class Solution {
public:
    int integerBreak(int n) {
        //The product close to the mean is the largest
        int ans = 0;
        for (int i = 2; i <= n; i++) {
            int piece_num = n / i;
            int extra = n % i;
            int temp_max = pow(piece_num, i - extra) * pow(piece_num + 1, extra);
            if (temp_max > ans)
                ans = temp_max;
        }
        return ans;
    }
};