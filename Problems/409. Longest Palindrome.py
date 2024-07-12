from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        result = 0
        for l, v in c.items():
            result += (v // 2) * 2
            c[l] = v % 2
        if any(c.values()):
            result += 1
        return result
