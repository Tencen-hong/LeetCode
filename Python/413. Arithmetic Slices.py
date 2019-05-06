class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res, count = 0, 1
        for i in range(1, len(A)-1):
            if A[i+1]-A[i] == A[i]-A[i-1]:
                res = res + count
                count += 1
            else:
                count = 1

        return res
