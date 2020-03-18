class Solution:
    '''
    对于这一天是否持股只有两种状态：持股状态（hold），没有持股状态（sell，cooldown）。
    对于当天持股状态时，至当天的为止的最大利润有两种可能：
        1、今天没有买入，跟昨天持股状态一样；
        2、今天买入，昨天是冷却期，利润是前天卖出股票时候得到的利润减去今天股票的价钱。 二者取最大值。
    对于当天未持股状态，至当天为止的最大利润有两种可能：
        1、今天没有卖出，跟昨天未持股状态一样；
        2、昨天持有股票，今天卖出了，利润是昨天持有股票时候的利润加上今天股票的价钱。 二者取最大值。

    '''

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        hold = [0]*len(prices)
        sell = [0]*len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            sell[i] = max(sell[i-1], hold[i-1] + prices[i])
            hold[i] = max(hold[i-1], sell[i-2] - prices[i])
        return sell[-1]
