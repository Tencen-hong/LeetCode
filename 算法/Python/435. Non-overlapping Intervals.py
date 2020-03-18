class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        curEnd = float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0] >= curEnd:
                curEnd = intervals[i][1]
            else:
                ans += 1

        return ans
