class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # Dynamic Programming and Binary Search
        # 1. Go through jobs in order of end time
        # 2. Find maximum amount of money that
        # can be made up to the jobs starting time
        # 3. Add this job to that amount
        # 4. Check if this amount is better than what is already there
        # 5. If it is, insert it into dp
        # 6. Since endTime is always increasing or staying the same
        # dp will always be sorted

        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]
        for start, end, profit in jobs:
            # Binary search for most profit
            i = bisect.bisect(dp, [start + 1]) - 1
            # Check for more money up to this point
            if dp[i][1] + profit > dp[-1][1]:
                # Note that dp[i][0] <= dp[-1][0]
                dp.append([end, dp[i][1] + profit])

        return dp[-1][1]
