class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Dynamic Programming
        # 1. Calculate maxSubarray of each ending index i
        # 2. dp[n] = maxSubarray up to this index
        # 3. dp[n+1] = max(dp[n] + v, v)

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            # If the max sum at index i
            # is found by adding previous numbers
            # use that.
            # Otherwise, we reset the sum
            # to the current index, because
            # the cumulative sum is lower than itself
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
