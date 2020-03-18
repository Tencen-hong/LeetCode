class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        for i in range(len(timePoints)):  # Turn into minutes from 0 to this time
            timePoints[i] = int(timePoints[i][0:2])*60 + int(timePoints[i][3:])

        timePoints = sorted(timePoints)  # Time sorted from small to large

        # Time difference before and after 0 o'clock
        ans = 1440 - timePoints[-1] + timePoints[0]

        for i in range(1, len(timePoints)):
            # Adjacent time difference
            ans = min(ans, timePoints[i] - timePoints[i-1])

        return ans
