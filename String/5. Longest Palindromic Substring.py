class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Dynamic Programming
        # 1. Create a dp for each starting and ending palindrome
        # 2. Base cases are one and two letter words

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            # One-letter base case
            dp[i][i] = True

        longest_palindrome = s[0]
        # Iterate by columns then rows upwards
        for end in range(1, n):
            for start in range(end - 1, -1, -1):
                # Check for two letter base case
                p_len = end - start + 1
                # Check palindrome edges
                if s[start] == s[end]:
                    # Valid palindrome
                    if p_len == 2 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        # Longest palindrome
                        if end - start + 1 > len(longest_palindrome):
                            longest_palindrome = s[start : end + 1]

        return longest_palindrome
