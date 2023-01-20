class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP
        # DP(i,j) = DP(i-1,j) + DP(i,j-1)
        # 1. Create a grid
        # 2. Fill out grid row by row

        if m == 1 or n == 1:
            return 1

        dp = defaultdict(lambda: defaultdict(int))
        dp[0][0] = 1
        print(dp)
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[m - 1][n - 1]
