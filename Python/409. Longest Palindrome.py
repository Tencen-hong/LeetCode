class Solution:
    '''
    最大回文子串的字母构成=出现偶数次的所有该字母集合 + 出现基数次的所有该字母中剔除掉1个该字母的集合 + 剩余字母中的随机某个字母。
    '''

    def longestPalindrome(self, s: str) -> int:
        d = collections.Counter(s)
        result = 0
        for item in d:
            number = d[item]
            need = number if number % 2 == 0 else number - 1
            d[item] -= need
            result += need
        if 1 in d.values():
            result += 1
        return result
