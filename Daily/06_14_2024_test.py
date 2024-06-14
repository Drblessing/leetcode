from collections import Counter


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        """Calculate the minimum number of increments to make all elements unique."""
        max_nums = max(nums)

        # Create a Counter object to store the frequency of each element in nums
        freq = Counter(nums)

        # Initialize the number of increments needed to 0
        minIncrements = 0

        # Iterate from 0 to maximum value in nums
        for i in range(0, max_nums + 1):
            # If the frequency of the current element is greater than 1
            if freq[i] > 1 and i != max_nums:
                # Calculate the number of increments needed to make the element unique
                increments = freq[i] - 1
                # Increment the element by 1 and add the number of increments to the total
                freq[i + 1] += increments
                minIncrements += increments

            # Check if we need to increment the last element
            if i == max_nums and freq[i] > 1:
                # Calculate the number of increments needed to make the element unique
                increments = freq[i] - 1

                # Since we're at the last element,
                # we need to increment every duplicate element by a different value
                # Therefore, we add the sum of the first n natural numbers to the total
                # We calculate the sum of the first n natural numbers using the formula n * (n + 1) / 2
                minIncrements += increments * (increments + 1) // 2

        return minIncrements


def test_minIncrementForUnique():
    solution = Solution()

    # Test 1
    nums = [1, 2, 2]
    assert solution.minIncrementForUnique(nums) == 1

    # Test 2
    nums = [3, 2, 1, 2, 1, 7]
    assert solution.minIncrementForUnique(nums) == 6

    # Test 3
    nums = [2, 2, 2, 1]
    assert solution.minIncrementForUnique(nums) == 3

    print("All tests passed.")
