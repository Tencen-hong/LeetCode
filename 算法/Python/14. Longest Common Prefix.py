class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:  # if strs is empty
            return ""

        prefix = strs[0]  # make prefix be the shortest one
        for str_ in strs:
            if len(str_) < len(prefix):
                prefix = str_

        for str_ in strs:  # find the common prefix
            for i in range(len(prefix)):
                if prefix[i] != str_[i]:
                    prefix = prefix[:i]
                    break
        return prefix
