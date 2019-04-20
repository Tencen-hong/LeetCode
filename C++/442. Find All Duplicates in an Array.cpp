class Solution
{
public:
    vector<int> findDuplicates(vector<int> &nums)
    {
        vector<int> ans;
        //归位
        for (int i = 0; i < nums.size();)
        {
            if (nums[i] != nums[nums[i] - 1])
            {
                swap(nums[i], nums[nums[i] - 1]);
            }
            else
            {
                i++;
            }
        }
        //不在其位，便是重复数字
        for (int i = 0; i < nums.size(); i++)
        {
            if ((nums[i] - 1) != i)
            {
                ans.push_back(nums[i]);
            }
        }
        return ans;
    }
};