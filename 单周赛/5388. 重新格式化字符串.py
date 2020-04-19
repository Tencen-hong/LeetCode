class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        number = []
        for ch in s:
            if ch.isdigit():
                number.append(ch)
            else:
                alpha.append(ch)
        res = []
        for i in range(min(len(alpha), len(number))):
            res.append(alpha[i])
            res.append(number[i])
        if abs(len(alpha) - len(number)) > 1:
            return ''
        if len(alpha) < len(number):
            res.insert(0, number[-1])
        elif len(number) < len(alpha):
            res.append(alpha[-1])

        return ''.join(res)
