class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[float('inf') for j in range(105)] for i in range(105)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(k):
                for length in range(1, n-i+1):
                    cost = 0
                    a = i
                    b = i+length-1
                    while a < b:
                        if s[a] != s[b]:
                            cost += 1
                        a += 1
                        b -= 1
                    dp[i+length][j+1] = min(dp[i+length][j+1], dp[i][j]+cost)

        return dp[n][k]
