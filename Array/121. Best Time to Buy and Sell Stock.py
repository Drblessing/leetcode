class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The max profit of
        # profits[i] = prices[i] - min(prices[:i])
        # 1. Iterate through prices
        # 2. Keep track of min seen up to i
        # 3. Calculate prices[i] - min seen
        # 4. Return max

        # 1.
        profit, min_price = 0, float("inf")
        n = len(prices)
        for price in prices:
            # 3.
            profit = max(profit, price - min_price)
            # 2.
            min_price = min(min_price, price)
        return profit
