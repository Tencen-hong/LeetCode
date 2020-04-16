class Solution:
    def mycmp(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] == b[0]:
            return 0
        else:
            return 1

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=functools.cmp_to_key(self.mycmp))
        # print(intervals)
        res = []
        for inter in intervals:
            if not res:
                res.append(inter)
            elif inter[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], inter[1])
            else:
                res.append(inter)
        return res
