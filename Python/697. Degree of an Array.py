class Solution:
    '''
    1.分别记录每个数字的每次出现的位置(第一个即是第一次出现的位置，最后一个即是最后一次出现的位置),
      同时记录最大出现频率
    2.找到最大出现频率的数字
    3.取这些数字的最短长度
    '''

    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_map = collections.defaultdict(list)
        deg = 0
        for k, v in enumerate(nums):
            nums_map[v].append(k)
            deg = max(deg, len(nums_map[v]))

        min_len = len(nums)
        for k, v in nums_map.items():
            if len(v) == deg:
                min_len = min(min_len, v[-1]-v[0]+1)
        return min_len
