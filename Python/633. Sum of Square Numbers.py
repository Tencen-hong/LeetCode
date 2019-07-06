class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        end = int(math.sqrt(c)+1)
        begin = 0
        while begin<=end:
            _sum = begin**2 + end**2 
            if _sum == c:
                return True
            elif _sum < c:
                begin += 1
            elif _sum > c:
                end -= 1
        return False
        '''
        all = set()
        idx = 0
        while idx*idx <= c:
            all.add(idx*idx)
            idx += 1
        for v in all:
            if (c-v) in all:
                return True
        return False
