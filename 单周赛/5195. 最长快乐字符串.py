class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        last = -1
        while sum([a, b, c]) > 0:
            f = True
            ma = max([a, b, c])
            if res[-2:] == 'aa':
                mix = min(b, c)
                if mix > 0:
                    if mix == b:
                        res += 'b'
                        b -= 1
                    elif mix == c:
                        res += 'c'
                        c -= 1
                else:
                    if mix == b and c > 0:
                        res += 'c'
                        c -= 1
                    elif mix == c and b > 0:
                        res += 'b'
                        b -= 1
            elif res[-2:] == 'bb':
                mix = min(a, c)
                if mix > 0:
                    if mix == a:
                        res += 'a'
                        a -= 1
                    elif mix == c:
                        res += 'c'
                        c -= 1
                else:
                    if mix == a and c > 0:
                        res += 'c'
                        c -= 1
                    elif mix == c and a > 0:
                        res += 'a'
                        a -= 1

            elif res[-2:] == 'cc':
                mix = min(a, b)
                if mix > 0:
                    if mix == a:
                        res += 'a'
                        a -= 1
                    elif mix == b:
                        res += 'b'
                        b -= 1
                else:
                    if mix == a and b > 0:
                        res += 'b'
                        b -= 1
                    elif mix == b and a > 0:
                        res += 'a'
                        a -= 1
            else:
                if ma > 0:
                    if ma == a:
                        res += 'a'
                        a -= 1
                    elif ma == b:
                        res += 'b'
                        b -= 1
                    elif ma == c:
                        res += 'c'
                        c -= 1

            if len(res) == last:
                break
            else:
                last = len(res)

        return res
