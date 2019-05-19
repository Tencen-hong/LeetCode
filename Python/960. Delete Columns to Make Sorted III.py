class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        dp = [1]*len(A[0])
        for j in range(1, len(A[0])):
            for i in range(j):
                if all(A[k][i] <= A[k][j] for k in range(len(A))):
                    dp[j] = max(dp[j], dp[i]+1)
        return len(A[0]) - max(dp)
