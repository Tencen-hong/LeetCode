class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        for i in range(1,len(s)):
            if len(s)%i != 0:
                continue
            times = len(s)//i
            if s[:i] * times == s:
                return True
        return False
        '''

        return (s*2)[1:-1].find(s) != -1
