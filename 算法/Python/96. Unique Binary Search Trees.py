class Solution:
    '''
    G(n)是n个数字的BST个数，注意数字是什么对结果没有影响
    F(n,i)是n个数字且以第i个数字为根的BST个数。
    f[n][i] = g[i-1]*g[n-i]
    g[n] = sum(f[n][i])
    其中f[n][i]可省略
    '''

    def numTrees(self, n: int) -> int:
        g = [0]*(n+1)
        g[0] = 1
        g[1] = 1
        for num in range(2, n+1):
            for i in range(1, num+1):
                g[num] += g[i-1]*g[num-i]

        return g[n]
