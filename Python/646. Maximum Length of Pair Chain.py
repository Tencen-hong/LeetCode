class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: (x[1]))
        res = 0
        end = [float('-inf'), float('-inf')]
        for i in range(len(pairs)):
            if pairs[i][0] > end[1]:
                res += 1
                end = pairs[i]
        return res
