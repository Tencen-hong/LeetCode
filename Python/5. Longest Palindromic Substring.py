class Solution:
    # from center expend
    def expendWithCenter(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        res = ""
        while i < len(s):
            if len(s) - i <= len(res)/2:  # if the length of left string shorter than answer,just cut it
                break
            # if the length of answer is odd , e.g. aba
            temp = Solution.expendWithCenter(s, i, i)
            if(len(res) < len(temp)):
                res = temp
            # if the length of answer is even, e.g abba
            temp = Solution.expendWithCenter(s, i, i+1)
            if(len(res) < len(temp)):
                res = temp

            i += 1
        return res
