class Solution {
public:
    void helper(vector<vector<int>> &ans, vector<int> &nums, vector<int> &subset, int start) {
        ans.push_back(subset);
        for (int i = start; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            helper(ans, nums, subset, i + 1);
            subset.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        //recurrence
        vector<vector<int>> ans;
        vector<int> subset;
        helper(ans, nums, subset, 0);
        return ans;
    }
};