class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def help(n, k, com, index):
            if 0 == k:
                res.append(com[:])
                return
            for i in range(index, n+1):
                help(n, k-1, com+[i], i+1)

        help(n, k, [], 1)
        return res
