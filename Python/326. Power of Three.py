class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        m = pow(3, 32)
        return n > 0 and m % n == 0
