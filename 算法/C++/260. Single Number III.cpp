class Solution
{
public:
    vector<int> singleNumber(vector<int> &nums)
    {
        int temp = 0;
        vector<int> res(2, 0);
        for (int i = 0; i < nums.size(); i++)
        {
            temp ^= nums[i];
        }
        int index = 1;
        while (index != 0)
        {
            if ((index & temp) != 0)
            {
                break;
            }
            index = index << 1;
        }

        for (int i = 0; i < nums.size(); i++)
        {
            if ((index & nums[i]) == 0)
            {
                res[0] ^= nums[i];
            }
            else
            {
                res[1] ^= nums[i];
            }
        }
        return res;
    }
};