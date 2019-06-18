class Solution:
    '''
    1.将每一行都做成set集合
    2.检查每个单词，是否是某个set集合的子集合

    '''

    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = set('qwertyuiop'), set(
            'asdfghjkl'), set('zxcvbnm')
        res = []
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                res.append(word)
        return res
