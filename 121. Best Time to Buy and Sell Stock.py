class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 1. Map: traverse each buy price and corresponding max sell price

        # 2. Traverse from end to start
        max_sell = prices[-1]
        max_profit = 0
        i = len(prices) - 2

        while i >= 0:
            max_sell = max_sell if max_sell>prices[i+1] else prices[i+1]
            max_profit = max_profit if max_profit>max_sell-prices[i] else max_sell-prices[i]
            i -= 1

        return max_profit
    


s = Solution()
prices = [7,6,4,3,1]
print(s.maxProfit(prices))