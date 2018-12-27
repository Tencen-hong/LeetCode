class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {

        if (nums.empty())
            return 0;

        const int len =  *max_element(nums.begin(), nums.end()); // the max num in nums used to be the length
        vector<int> value(len + 10, 0);
        //value store num and corresponding value
        for (auto &it : nums) {
            value[it] += it;
        }
        //dp store max_value before index i(include i)
        vector<int> dp(len + 10, 0);
        dp[0] = value[0];
        dp[1] = value[1];
        //calculate the current dp  in max(dp[1 position in front of current index],dp[2 position in front of current index] + value[current position])

        for (int i = 2; i < dp.size(); i++) {
            dp[i] = max(dp[i - 1], dp[i - 2] + value[i]);
        }

        return dp.back();
    }
};