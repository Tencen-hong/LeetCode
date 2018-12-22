class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        sub = ""
        max_len = 0
        for i in range(len(s)):
            start = sub.find(s[i], 0, len(sub))

            if start == -1:  # substring don't contain s[i]
                sub += s[i]
            else:  # s[i] in substring
                if(start+1 < len(sub)):
                    # dropout string before s[i] in substring
                    sub = sub[(start+1):]
                else:
                    sub = ""
                sub += s[i]
            if len(sub) > max_len:
                max_len = len(sub)

        return max_len
