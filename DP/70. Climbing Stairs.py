class Solution:
    def climbStairs(self, n: int) -> int:
        # climbStairs(n) = climbStairs(n-2) + climbStairs(n-1)
        # Optimal substructure property
        # therefore we can use DP
        # climbStairs(1) = 1
        # climbStairs(2) = 2
        #
        # Solution
        # 1. Calculate base solutions
        # 2. Iterate over number of stairs and calculate final answer

        if n == 1:
            return 1

        a, b = 1, 2
        for i in range(n - 2):
            a, b = b, a + b
        return b
