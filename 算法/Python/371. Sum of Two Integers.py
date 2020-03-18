class Solution:
    def getSum(self, a: int, b: int) -> int:
        for _ in range(32):
            a, b = a ^ b, (a & b) << 1
        return a if a & 0x10000000 else a & 0xffffffff
