class Solution:
    def fib(self, N: int) -> int:
        F = [0]*(N+2)
        F[0] = 0
        F[1] = 1
        for i in range(2, N+1):
            F[i] = F[i-1]+F[i-2]
        return F[N]
