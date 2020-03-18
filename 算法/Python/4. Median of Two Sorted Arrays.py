class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # make len(nums1) < len(nums2)
        if(len(nums1) > len(nums2)):
            return Solution.findMedianSortedArrays(self, nums2, nums1)

        m = len(nums1)
        n = len(nums2)
        lo, hi = 0, m

        while lo <= hi:
            # split left of middle to 2 groups i and j
            # i-1,j-1 point to middle- , i,j point to middle+
            i = int((lo+hi)/2)
            j = int((m+n+1)/2 - i)
            # if middle+ < middle- : i need be larger to point middle+
            if i < m and nums1[i] < nums2[j-1]:
                lo = i + 1
            # if middle- > middle+ : i-1 need be smaller to point middle-
            elif i > 0 and nums1[i-1] > nums2[j]:
                hi = i - 1
            else:  # i-1,j-1 point to middle- ; i,j point to middle+ ; all middle- <= middle+
                if i == 0:
                    leftmax = nums2[j-1]  # all elements before middle in nums2
                elif j == 0:
                    leftmax = nums1[i-1]  # all elements before middle in nums1
                else:
                    leftmax = max(nums1[i-1], nums2[j-1])
                # odd
                if int((m+n) % 2 == 1):
                    return leftmax

                if i == m:
                    # i out of index range , rightmin in nums2
                    rightmin = nums2[j]
                elif j == n:
                    # j out of index range , rightmin in nums1
                    rightmin = nums1[i]
                else:
                    rightmin = min(nums1[i], nums2[j])
                # even
                return (leftmax + rightmin)/2
