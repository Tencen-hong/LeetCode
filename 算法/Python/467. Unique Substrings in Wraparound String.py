class Solution:
    '''
    比如abcd这个字符串，以d结尾的子字符串有abcd, bcd, cd, d，那么我们可以发现bcd或者cd这些以d结尾的字符串的子字符串都包含在abcd中，那么我们知道以某个字符结束的最大字符串包含其他以该字符结束的字符串的所有子字符串，那么题目就可以转换为分别求出以每个字符(a-z)为结束字符的最长连续字符串长度就行了。

    '''

    def findSubstringInWraproundString(self, p: str) -> int:
        cnt = [0]*26
        length = 0
        for i in range(len(p)):
            if i > 0 and ord(p[i]) == ord(p[i-1]) + 1 or ord(p[i]) == ord(p[i-1]) - 25:
                length += 1
            else:
                length = 1
            cnt[ord(p[i]) - ord('a')] = max(cnt[ord(p[i]) - ord('a')], length)
        return sum(cnt)
