class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                t1 = s[:i] + s[i+1:]
                t2 = s[:j] + s[j+1:]
                return t1[::-1] == t1 or t2[::-1] == t2
            i += 1
            j -= 1
        return True
