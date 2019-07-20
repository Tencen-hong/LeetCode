class Solution:
    '''
    按照区间起点排序，然后二分查找
    '''

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        invs = sorted((x[0], i) for i, x in enumerate(intervals))
        ans = []
        for x in intervals:
            idx = bisect.bisect_right(invs, (x[1],))
            ans.append(invs[idx][1] if idx < len(invs) else -1)
        return ans
