class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP
        # rob(nums) = max(rob(nums[:-2] + nums[-1]),rob(nums[:-1]))
        #
        # Solution
        # 1. Calculate base cases of rob
        # 2. Iterate through nums using DP formula

        n = len(nums)
        if n == 1:
            return nums[0]

        elif n == 2:
            return max(nums)

        dp = [nums[0], nums[1]]

        for i in range(2, n):
            money = max(dp[-1], max(dp[0 : i - 1]) + nums[i])
            dp.append(money)

        return dp[-1]
