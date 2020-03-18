class Solution:
    '''
    分别用3个指针指向乘以235时最小的3个数
    '''

    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        i2 = i3 = i5 = 0
        j = 1
        while j < n:
            m = min(ans[i2] * 2, ans[i3] * 3, ans[i5] * 5)
            if m == ans[i2] * 2:
                i2 += 1
            if m == ans[i3] * 3:
                i3 += 1
            if m == ans[i5] * 5:
                i5 += 1
            ans.append(m)
            j += 1
        print(ans)
        return ans[-1]
