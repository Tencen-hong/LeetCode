class Solution:
    '''
     设定len(p) 大小的滑动窗口
     统计窗口内的字符频率
     若=p的统计，则加入起始位置到结果中
     减去最老字符的一次频率
    '''

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                res.append(i-len(p)+1)
            sCounter[s[i-len(p)+1]] -= 1
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]

        return res
