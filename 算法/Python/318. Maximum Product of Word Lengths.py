class Solution:
    '''
    1. 用左移1的位置表示一个单词中出现了哪些字母
    2. 和1的结果一样的最大的单词长度存入字典
    3. 字典的2个key所有的对应位都不为1(2个单词中没有出现过相同的字母),计算长度的乘积
    4. 返回乘积的最大值，若不存在,返回0
    '''

    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for word in words:
            mask = 0
            for w in word:
                mask |= 1 << (ord(w) - ord('a'))
            d[mask] = max(d.get(mask, 0), len(word))

        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
