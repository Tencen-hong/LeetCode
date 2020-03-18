class Solution:
    '''
    遍历数组找高度最高的柱子，
    将数分成2半
    '''

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        mx = height.index(max(height))
        res = 0
        # 从左向右遍历，lp记录左侧柱子标尺
        lp = 0
        for i in range(mx):
            if height[i] > lp:
                lp = height[i]
            else:
                res += lp - height[i]
        # 从右向左遍历，rp记录右侧柱子标尺
        rp = 0
        for j in range(len(height)-1, mx, -1):
            if height[j] > rp:
                rp = height[j]
            else:
                res += rp - height[j]
        return res
