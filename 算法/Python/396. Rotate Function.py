class Solution:
    '''
    由于每一次循环迭代都是循环右移一位操作
    F(k+1) = F(k) - (n-1)*B[n-1] + (sum(A) - B[n-1])
           = F(k) + sum(A) - n*B[n-1]
    '''

    def maxRotateFunction(self, A: List[int]) -> int:
        if not A:
            return 0
        F = []
        n = len(A)
        t = 0
        for i in range(n):
            t += i * A[i]
        F.append(t)
        s = sum(A)
        for i in range(1, n):
            F.append(F[-1] + s - n * A[n-i])
        return max(F)
