class Solution:
    '''
    其基本思想是利用栈尽量维持一个递增的序列，也就是说将字符串中字符依次入栈，如果当前字符串比栈顶元素小，并且还可以继续删除元素，那么就将栈顶元素删掉，这样可以保证将当前元素加进去一定可以得到一个较小的序列．如果这样得到的是一个空串那就手动返回０．还有一个需要注意的是字符串首字符不为０

    '''

    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for val in num:
            while stack and k > 0 and val < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(val)

        while stack and k > 0:
            stack.pop()
            k -= 1

        res = ''.join(stack).lstrip('0')

        return res if res else '0'
