class Solution:
    '''
    栈中存放nums的索引
    遍历数组： 取出栈顶元素index，如果nums[index]<nums[i]，那么nums[i]就是nums[index]的第一个大的数，将当前的索引i存入栈中。
    后面元素的第一个大的数 可能在列表前面， 所以要再次从头遍历列表(此时，靠近栈顶的是后面的元素)。
    '''

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        for i in list(range(len(nums)))*2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
