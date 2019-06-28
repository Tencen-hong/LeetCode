class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = ""
        carry = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        i = 0
        while i < len(num1) or i < len(num2):
            s = 0
            if i < len(num1):
                s += int(num1[i])
            if i < len(num2):
                s += int(num2[i])
            s += carry
            carry = s//10
            ret += str(s % 10)
            i += 1
        if carry:
            ret += '1'
        return ret[::-1]
