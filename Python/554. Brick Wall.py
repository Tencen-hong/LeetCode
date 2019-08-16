class Solution:
    '''
    使用一个哈希表来建立每一个断点的长度和其出现频率之间的映射，这样只要我们从断点频率出现最多的地方劈墙，损坏的板砖一定最少。
    '''

    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall:
            return 0
        count = 0
        map_ = {}
        for w in wall:
            brickPoint = 0
            for j in range(len(w)-1):
                brickPoint += w[j]
                map_[brickPoint] = map_.get(brickPoint, 0)+1
                count = max(count, map_.get(brickPoint))

        return len(wall) - count
