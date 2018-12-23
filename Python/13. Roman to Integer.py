class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # define a roman dict
        dictionary = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return dictionary[s]

        res = 0
        i = 0
        while i < len(s):
            # if s[i]<s[i+1] like IV=4
            if i+1 < len(s) and dictionary[s[i]] < dictionary[s[i+1]]:
                res += dictionary[s[i+1]] - dictionary[s[i]]
                i += 2
            else:
                res += dictionary[s[i]]
                i += 1
        return res
