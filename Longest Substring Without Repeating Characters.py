class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        o = 0

        # left index of substring
        l = 0

        for i, v in enumerate(s):

            if v not in seen:
                o = max(o, i - l + 1)

            else:
                if seen[v] < l:
                    o = max(o, i - l + 1)

                else:
                    l = seen[v] + 1

            seen[v] = i

        return o


