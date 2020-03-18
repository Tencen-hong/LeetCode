class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)  # convert str to list
        for i in range(0, len(s), 2*k):  # Traversing s ,step = 2*k
            if i-1 <= 0:
                s[i:i+k] = s[i+k-1::-1]  # reverse (i,i+k),when at beginning
            else:
                s[i:i+k] = s[i+k-1:i-1:-1]  # reverse(i,i+k)
        return ''.join(s)
