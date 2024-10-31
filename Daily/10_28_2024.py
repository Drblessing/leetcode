from typing import List
import unittest


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """Find the longest square streak subsequence in nums.
        The order in the subsequence does not matter.
        Length >= 2 or return -1 if not found.
        """

        # since order does not matter in the subsequence, we can turn
        # the list into a set to speed-up the search
        nums_set = set(nums)
        seen = set()
        longest_streak = 0
        nums.sort()
        for num in nums:
            current_streak = 0
            cur = num
            while cur in nums_set:
                current_streak += 1
                cur *= cur
            longest_streak = max(longest_streak, current_streak)
        return longest_streak if longest_streak >= 2 else -1


class TestLongestSquareStreak(unittest.TestCase):
    def test_longest_square_streak(self):
        sol = Solution()
        self.assertEqual(sol.longestSquareStreak([4, 3, 6, 16, 8, 2]), 3)
        self.assertEqual(sol.longestSquareStreak([2, 3, 5, 6, 7]), -1)


if __name__ == "__main__":
    unittest.main()
