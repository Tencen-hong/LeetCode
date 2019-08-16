class Solution:
    '''
    [.., a.., b..] 
    sum[a:b] = k  = prefix_sum[b] - prefix_sum[a] ==>
    prefix_sum[b] - k = prefix_sum[a]
    用dict存储前缀和的出现次数
    如果当前位置之前有相加和为sum-k的位置，则这两个位置之间的数字相加和为k，dick[sum-k]
    '''

    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        d[0] = 1
        sum_ = 0
        res = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ - k in d:
                res += d[sum_ - k]
            d[sum_] = d.get(sum_, 0) + 1
        return res
