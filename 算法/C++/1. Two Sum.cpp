
class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {

        vector<int> res;
        unordered_map<int, int> mmap;
        for (int i = 0; i < nums.size(); i++) {
            int left = target - nums[i];
            if (mmap.count(left) > 0) {
                res.push_back(mmap[left]);
                res.push_back(i);
                return res;
            }
            mmap[nums[i]] = i;
        }

        return res;
        
    }
};

//map.count() faster than map.find()