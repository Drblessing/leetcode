from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        n = len(nums)

        dp = [0] * n

        dp[-1] = nums[-1]

        dq = deque()

        dq.append(n - 1)

        for i in range(n - 2, -1, -1):

            if dq[0] - i > k: dq.popleft()

            dp[i] = nums[i] + dp[dq[0]]

            while len(dq) and dp[dq[-1]] < dp[i]: dq.pop()

            dq.append(i)

        return dp[0]