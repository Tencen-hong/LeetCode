class Solution:
    '''
    因为数组的排序后正确顺序应该是arr[i]处的数是i。所以，遍历数组，每次将最大的那个值标记为maxn，maxn必须在i处才能满足对0～i数字排序后能够恰好是正确的位置，此时ans+1，表示前面的可以组为一个“块”，最后ans即为所求的值
    '''

    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        maxn = 0
        for i in range(len(arr)):
            maxn = max(maxn, arr[i])
            if maxn == i:
                ans += 1
        return ans
