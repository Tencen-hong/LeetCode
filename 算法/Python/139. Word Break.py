class Solution:
    '''
    我们用dp[i]表示字符串s[:i] 是否可被拼接而成，那么dp[i]如何求呢，我们遍历wordDict,如果对于每一个word,s[:i-len(word)]可以被拼接而成，那么s[:i]可由s[:i-len(word)]和word拼接而成。设置dp[0] 为True即可解决问题。
    '''

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(dp)):
            for word in wordDict:
                if i-len(word) >= 0:
                    dp[i] = dp[i-len(word)] or dp[i] if s[i -
                                                          len(word):i] == word else dp[i]
        return dp[-1]
