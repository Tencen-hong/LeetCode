class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = 1

        "if negative opposite it and mark a sign"
        if x < 0:
            x = -x
            flag = -1

        "int to string"
        x = str(x)

        "reverse the string"
        x = x[::-1]

        "string and flag to int"
        res = int(int(x) * flag)

        "if overflow return 0"
        if (res > 2 ** 31 - 1 or res < -2 ** 31):
            return 0

        return res
