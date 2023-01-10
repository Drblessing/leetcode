# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 1. Binary Search
        # 2. If false, search upper half
        # 3. If true, search lower half
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            if isBadVersion(mid):
                r = mid - 1

            else:
                l = mid + 1

        return l
