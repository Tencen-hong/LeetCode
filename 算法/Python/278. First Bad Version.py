# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            elif isBadVersion(mid) == True and isBadVersion(mid - 1) == True:
                r = mid - 1
            elif isBadVersion(mid) == False and isBadVersion(mid-1) == False:
                l = mid + 1
