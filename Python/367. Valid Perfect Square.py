class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        l=1
        r = num
        while l<=r:
            mid = (l+r)//2
            if mid**2 == num:
                return True
            if mid**2 < num:
                l = mid+1
            elif mid**2 > num:
                r = mid-1
        return False
    