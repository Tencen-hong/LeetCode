class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        // make nums1.size()<nums2.size()
        int m = nums1.size();
        int n = nums2.size();
        int lo = 0, hi = m;
        // i+j = (m+n)/2,   (left,middle,right) divide left to 2 groups i and j,
        int leftmax, rightmin; // if m+n is even  then  leftmax = middle- ,rightmin = middle+ ,
        while (lo <= hi) {
            int i = (lo + hi) / 2; // the middle in nums1
            int j = (m + n + 1) / 2 - i ; //the rest of numbers in (combined nums1&nums2 )
            if (i > 0 && nums1[i - 1] > nums2[j]) { // if group i too large
                hi = i - 1;
            } else if (i < m && nums1[i] < nums2[j - 1]) { // if group j too large
                lo = i + 1;
            } else {
                //middle-  be the bigger one in (nums1[i-1],nums2[j-1])
                if (i == 0) { // dropout nums1
                    leftmax = nums2[j - 1];
                } else if (j == 0) { //dropout nums2
                    leftmax = nums1[i - 1];
                } else {
                    leftmax = max(nums1[i - 1], nums2[j - 1]);
                }

                if ((m + n) % 2 == 1)
                    return leftmax;
                // middle+  be the smaller one in (nums1[i],nums2[j])
                if (i == m) { // all contain nums1
                    rightmin = nums2[j];
                } else if (j == n) { // all contain nums2
                    rightmin = nums1[i];
                } else {
                    rightmin = min(nums1[i], nums2[j]);
                }
                return (leftmax + rightmin) / 2.0;
            }

        }
    }
};