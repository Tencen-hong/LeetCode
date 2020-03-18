class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d, key=lambda x: (-len(x), x))
        for v in d:
            j = 0
            for i in range(len(s)):
                if j < len(v) and s[i] == v[j]:
                    j += 1
            if j == len(v):
                return v
        return ""
