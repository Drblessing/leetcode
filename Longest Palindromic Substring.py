class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        lp = s[0]

        for end in range(0, n):

            for start in range(end - 1, -1, -1):

                p_len = end - start + 1

                # element wise comparison
                if s[start] == s[end]:

                    if p_len == 2 or dp[start + 1][end - 1] == True:
                        dp[start][end] = True

                        lp = max(lp, s[start:end + 1], key=len)

        return lp


