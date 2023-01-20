class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic Programming
        # 1. dp[n] = dp[n-1] + dp[n-2]
        # 2. Base Cases: dp[1] = 1, dp[2] = 2

        dp = []
        dp.extend([0, 1, 2])
        if n == 1 or n == 2:
            return dp[n]

        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]
