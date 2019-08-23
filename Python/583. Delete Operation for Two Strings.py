class Solution:
    '''
    dp[i][j]表示s1[0:i]和s2[0:j]的最长公共子串，那么我们只需要在字符对上时，dp[i][j] = dp[i - 1][j - 1] + 1，对不上时，dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])就行了.

    '''

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1]
                                       [j], dp[i][j] + (word1[i] == word2[j]))
        return m + n - 2 * dp[m][n]
