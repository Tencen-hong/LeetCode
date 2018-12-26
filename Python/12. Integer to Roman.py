class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000, }
        res = ""
        a = int(num/1000)  # Thousand number
        b = int(num % 1000/100)  # hundreds number
        c = int(num % 1000 % 100/10)  # Ten number
        d = int(num % 10)  # Single number

        # hard decoding
        if a:
            res += 'M'*a

        if b == 9:
            res += "CM"
        elif b >= 5:
            res += 'D' + 'C'*(b-5)
        elif b == 4:
            res += "CD"
        elif b > 0:
            res += 'C'*b

        if c == 9:
            res += "XC"
        elif c >= 5:
            res += 'L' + 'X'*(c-5)
        elif c == 4:
            res += "XL"
        elif c > 0:
            res += 'X'*c

        if d == 9:
            res += "IX"
        elif d >= 5:
            res += 'V' + 'I'*(d-5)
        elif d == 4:
            res += "IV"
        elif d > 0:
            res += 'I'*d

        return res
