class Solution:
    '''
    首先，将输入转换为一组set。需要O(N)，然后我们可以在O(1)时间查找是否有一个特定的数字。
    如果x是Sequence的开始(即x-1不在集合中)，则测试y=x+1，x+2，x+3，.停在第一个数字y不在set中。
    Sequence的长度就是y-x，我们用它更新我们的全局最佳值。因为我们只检查了一次，所以整体是O(N)。
    '''

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
