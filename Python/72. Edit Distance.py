class Solution:
    '''
        从两个字符串最后的位置开始考虑
        如果最后两个字符(i,j)相等，那么最后两个字符就不需要配对，等于minDistance(i-1,j-1)
        如果最后两个字符不等，则需要处理，分为3种情况
            1.如果word1[i-1] 和 word2[j] 可以配对，删除word1[i]即可
            2.如果word1[i] 和 word2[j-1] 可以配对，在word1后面加上word2[j]即可
            3.如果word1[i-1] 和 word2[j-1] 可以配对，把word1[i]修改成word2[j]即可
    '''

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for i in range(len(word2))] for j in range(len(word1))]

        def helper(i, j):
            if i == -1:
                return j+1
            if j == -1:
                return i+1
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = helper(i-1, j-1)
            else:
                dp[i][j] = 1 + min(helper(i-1, j),
                                   helper(i, j-1), helper(i-1, j-1))
            return dp[i][j]

        return helper(len(word1)-1, len(word2)-1)
