class Solution:
    '''
    dp[amount] 表示 达到amount的钱有 dp[amount]种方法
    '''

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for target in range(1, amount+1):
                if target >= coin:  # 保证索引>0
                    dp[target] += dp[target-coin]
        return dp[amount]
