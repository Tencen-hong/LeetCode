class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        res, end = 0, float('-inf')
        for interval in points:
            if end < interval[0]:
                res += 1
                end = interval[1]
        return res
