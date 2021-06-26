class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Target sum
        s = sum(nums)

        # Odd = false
        if s % 2 == 1: return False

        # Target/2 for subset
        s = int(s / 2)

        # Init dp
        dp = [False] * (s + 1)

        dp[0] = True

        # Iterate through nums
        # change dp to true if
        # subset can equal that number
        for n in nums:

            # Iterate backwards
            for i in range(s, n - 1, -1):
                # dp[i] = true if dp[i-num] = true

                dp[i] = dp[i] or dp[i - n]

        return dp[s]















