class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP
        # 1. dp[amount] = min number of coins to reach amount
        # 2. Start at 0 and work your way up through 0 to amount

        # Init dp
        # Default value is infinity
        dp = defaultdict(lambda: float("inf"))
        dp[0] = 0
        for tmp_amount in range(1, amount + 1):
            # Check each coin
            for coin in coins:
                if coin <= tmp_amount:
                    dp[tmp_amount] = min(dp[tmp_amount - coin] + 1, dp[tmp_amount])
        return dp[amount] if dp[amount] != float("inf") else -1
