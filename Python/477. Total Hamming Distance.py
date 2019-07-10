class Solution:
    '''
    对于所有数字中的某一位，在两两比对时如果两者不同则其为总汉明距离贡献为1，如果相同则贡献为0。这样该位为0的数字和该位为1的数字可分为两个集合，它们互相之间都能为总汉明距离贡献1，而集合内部对总汉明距离没有贡献，因此将该位为0的个数和为1的个数相乘即可得出该位对总汉明距离的贡献。这样遍历整个int的32位即可求出总汉明距离
    '''

    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            a, b = 0, 0
            for n in nums:
                if (n >> i) & 1 == 1:
                    a += 1
                else:
                    b += 1
            res += a * b
        return res
