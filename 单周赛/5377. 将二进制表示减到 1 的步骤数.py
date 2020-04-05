class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        while s != '1':
            ans += 1
            if s[-1] == '1':
                s = self.plus(s)
            else:
                s = self.divide(s)
        return ans

    def divide(self, s):
        return s[:-1]

    def plus(self, s):
        carry = 1
        new_s = ''
        for ch in s[::-1]:
            t = carry + int(ch)
            carry = 0
            if t > 1:
                new_s += '0'
                carry = 1
            else:
                new_s += str(t)
        if carry == 1:
            new_s += '1'
        return new_s[::-1]
