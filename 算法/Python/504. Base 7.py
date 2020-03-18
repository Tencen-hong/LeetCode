class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        num1 = abs(num)
        res = ''
        while num1 > 0:
            res = str(num1 % 7) + res
            num1 //= 7
        if num > 0:
            return res
        else:
            return '-' + res
