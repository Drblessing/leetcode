import unittest


class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        """Calculated the sum of absolute differences for each index in a list."""
        n = len(nums)
        res = [0] * n
        for i in range(1, n):
            res[0] += nums[i] - nums[0]
        for i in range(1, n):
            res[i] = (
                res[i - 1]
                + (nums[i] - nums[i - 1]) * i
                - (nums[i] - nums[i - 1]) * (n - i)
            )
        return res


class TestSolution(unittest.TestCase):
    def test_getSumAbsoluteDifferences(self):
        solution = Solution()

        # Test Case 1
        nums1 = [2, 3, 5]
        expected1 = [4, 3, 5]
        self.assertEqual(solution.getSumAbsoluteDifferences(nums1), expected1)

        # Test Case 2
        nums2 = [1, 4, 6, 8, 10]
        expected2 = [24, 15, 13, 15, 21]
        self.assertEqual(solution.getSumAbsoluteDifferences(nums2), expected2)


# This is needed to run the tests if the file is run directly
if __name__ == "__main__":
    unittest.main()
