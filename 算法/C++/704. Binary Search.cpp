class Solution {
public:
    int search(vector<int>& nums, int target) {
        int hi = nums.size();
        int lo = 0;
        // Binary search
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                lo = mid + 1;
            else if (nums[mid] > target)
                hi = mid - 1;
        }
        return -1;
    }
};