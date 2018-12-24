class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_length = len(s)
        if numRows == 1 or s_length < 2:  # numrows too small or s too short
            return s

        interval = numRows - 2
        res = ""
        for i in range(numRows):  # for each row
            s_pos = i
            while s_pos < s_length:
                res += s[s_pos]  # add full column character postion
                s_pos = s_pos + numRows + interval  # next full column character

                if i != 0 and i != numRows-1:  # in zigzag shape character
                    if s_pos - (2*i) < s_length:
                        res += s[s_pos - (2*i)]  # add zigzag shape character

        return res
