class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        x = math.log(num, 4)
        return 4**x == 4**int(x)
