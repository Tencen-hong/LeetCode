class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        res = 0

        if x < 0:
            x = -x
            flag = -1

        while True:
            if (x <= 0):
                break
            res = int(res * 10 + x % 10)
            x = int(x / 10)

        res = flag * res

        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        
        return res
