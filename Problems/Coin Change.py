class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp
        dp = [float('inf')] * (amount + 1)

        # Init
        dp[0] = 0

        # Iterate throgh dp
        for i, v in enumerate(dp):

            # Iterate through coins
            for coin in coins:

                # Valid index
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[-1] == float('inf'): return -1

        return dp[-1]