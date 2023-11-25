"""Calculates sum of absolute differences in a list and tests the solution."""

import unittest


class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        """
        Calculate the sum of absolute differences for each index in a list.
        The absolute difference for an index i is the sum of the absolute difference between nums[i] and all other elements in the list.
        """
        n = len(nums)
        # Create a list of zeros with the same length as nums
        res = [0] * n
        # Calculate the sum of absolute differences for the first element
        for i in range(1, n):
            res[0] += nums[i] - nums[0]
        # Calculate the sum of absolute differences for the rest of the elements
        for i in range(1, n):
            res[i] = (
                res[i - 1]
                # Add the difference between the current element and the previous element, multiplied by the index
                + (nums[i] - nums[i - 1]) * i
                # Subtract the difference between the current element and the previous element, multiplied by the number of elements after the current element
                - (nums[i] - nums[i - 1]) * (n - i)
            )
        return res


class TestSolution(unittest.TestCase):
    def test_getSumAbsoluteDifferences(self):
        """Test the getSumAbsoluteDifferences method.

        Optional plotz says to frobnicate the bizbaz."""
        solution = Solution()

        # Test Case 1
        nums1 = [2, 3, 5]
        expected1 = [4, 3, 5]
        # Assert that the method returns the expected result for the first test case
        self.assertEqual(solution.getSumAbsoluteDifferences(nums1), expected1)

        # Test Case 2
        nums2 = [1, 4, 6, 8, 10]
        expected2 = [24, 15, 13, 15, 21]
        # Assert that the method returns the expected result for the second test case
        self.assertEqual(solution.getSumAbsoluteDifferences(nums2), expected2)


# This is needed to run the tests if the file is run directly
if __name__ == "__main__":
    unittest.main()
