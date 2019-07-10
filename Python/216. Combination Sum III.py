class Solution:
    '''
    回溯，每次递归选取的树比上一次要大
    '''

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k < 0 or k > 9*n:
            return []
        if k == 0 and n != 0:
            return []

        result = []
        temp = []
        self.hs(k, n, temp, result, 1)
        return result

    def hs(self, kk, nn, temp, result, m):
        if kk == 0 and nn == 0:
            result.append(temp[:])
            return
        if kk <= 0 or nn <= 0:
            return
        for i in range(m, 10):
            self.hs(kk-1, nn-i, temp+[i], result, i+1)
