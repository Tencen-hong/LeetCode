class Solution {
public:
    // compare (string1 concatenate string2 , string2 concatenate string1) if the former > the the latter, we think string1 is bigger
    static bool cmp1(string a, string b) {
        return a + b > b + a;
    }
    string largestNumber(vector<int>& nums) {
        vector<string> nums_;
        // convert to string
        for (int i = 0; i < nums.size(); i++) {
            nums_.push_back(to_string(nums[i]));
        }
        sort(nums_.begin(), nums_.end(), cmp1);
        string res;
        // concatenate all elements
        for (int i = 0; i < nums_.size(); i++)
            res += nums_[i];
        return nums_[0] == "0" ? "0" : res;
    }

};