from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """Sorts the array arr1 according to the order of arr2."""

        # Count the frequency of each element in arr1
        count = Counter(arr1)

        # Initialize the results array
        result = []

        # Iterate over each element in arr2
        for num in arr2:
            # Add the elements the correct frequency of times
            result.extend([num] * count.pop(num))

        # Add the remaining elements in sorted order
        result.extend(sorted(count.elements()))

        return result


def test_relativeSortArray():
    solution = Solution()

    # Test 1
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    assert solution.relativeSortArray(arr1, arr2) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

    # Test 2
    arr1 = [28, 6, 22, 8, 44, 17]
    arr2 = [22, 28, 8, 6]
    assert solution.relativeSortArray(arr1, arr2) == [22, 28, 8, 6, 17, 44]

    # Test 3
    arr1 = [28, 6, 22, 8, 44, 17]
    arr2 = [22, 28, 8, 6, 17, 44]
    assert solution.relativeSortArray(arr1, arr2) == [22, 28, 8, 6, 17, 44]

    print("All tests passed.")
    return True
