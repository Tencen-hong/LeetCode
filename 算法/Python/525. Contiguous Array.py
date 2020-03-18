class Solution:
    '''
首先从头开始遍历，如果当前值是0就sum-1，否则就sum+1.这样如果得到了一个sum就知道在此之前出现了1的个数和0的个数的差值。因此，当后面该sum再次出现的时候，我们就知道了这个差值再次出现，也就是说，从第一次这个差值出现和第二次这个差值出现之间0和1的个数是一样多的。
需要注意的是字典应该有个初始化值，代表在刚开始的时候没有任何元素的位置是-1，否则后面出现0的时不能和最开始的位置求位置差。
    '''

    def findMaxLength(self, nums: List[int]) -> int:
        total_sum = 0
        index_map = {}
        index_map[0] = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                total_sum -= 1
            elif num == 1:
                total_sum += 1
            if total_sum in index_map:
                res = max(res, i - index_map[total_sum])
            else:
                index_map[total_sum] = i

        return res
