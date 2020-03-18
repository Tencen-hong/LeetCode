class Solution:
    '''
    找个标志位flag，记下前一个做差的符号，遍历数组，用本次的差和flag相比，本次的差是0就忽略掉，本次的差和之前一样也忽略掉（其实是相当于在子队列里保当前的最后元素，剔除前一个），和之前不一样就说明是子序列的元素。
    '''

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        flag = 0
        for i in range(1, len(nums)):
            a = nums[i] - nums[i-1]
            if a != 0:
                a = a//abs(a)
            else:
                continue
            if a != flag:
                res += 1
            flag = a
        return res
