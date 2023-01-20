class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # DP
        # 1. Calculate target sum
        # 2. Iterate through each num
        # 3. Iterate backwards from target to 0
        # to avoid reusing coins

        s = sum(nums)
        target = int(sum(nums) / 2)
        # Can't split odd sum
        if s % 2 == 1:
            return False

        dp = [False] * (target + 1)
        dp[0] = True

        # Iterate through nums one at a time to
        # not reuse coins
        for num in nums:
            # Iterate backwards to avoid reuse
            for amount in range(target, num - 1, -1):
                dp[amount] = dp[amount - num] or dp[amount]
        return dp[target]
