class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c, r, o, a, k = 0, 0, 0, 0, 0
        res = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            elif ch == 'k':
                k += 1
            else:
                return -1
            if r > c or o > r or a > o or k > a:
                return -1

            res = max(res, c)
            if k == 1:
                c -= 1
                r -= 1
                o -= 1
                a -= 1
                k -= 1
        if c:
            return -1
        return res
