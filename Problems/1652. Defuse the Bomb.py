from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Decrypts the given code array based on the integer k.

        If k > 0, sums the next k elements for each index.
        If k < 0, sums the previous |k| elements for each index.
        If k == 0, returns an array of zeros.

        Parameters:
        code (List[int]): The list of integers to decrypt.
        k (int): The number indicating how many positions to sum.

        Returns:
        List[int]: The decrypted array.
        """
        n = len(code)
        result = [0] * n  # Initialize result array with zeros

        # Case when k is zero, return an array of zeros
        if k == 0:
            return result

        if k > 0:
            # Traverse each index to calculate the sum of the next k elements
            for current_index in range(n):
                current_sum = 0  # Initialize sum for the current index
                next_index = current_index
                for _ in range(k):
                    # Move to the next element in a circular manner
                    next_index = (next_index + 1) % n
                    current_sum += code[next_index]
                result[current_index] = current_sum
        else:
            # Case when k is negative: sum the previous |k| elements
            num_elements = -k  # Convert k to a positive number
            for current_index in range(n):
                current_sum = 0  # Initialize sum for the current index
                prev_index = current_index
                for _ in range(num_elements):
                    # Move to the previous element in a circular manner
                    prev_index = (prev_index - 1) % n
                    current_sum += code[prev_index]
                result[current_index] = current_sum

        return result


# Test cases
import unittest


class TestSolution(unittest.TestCase):
    def test_decrypt(self):
        solution = Solution()
        self.assertEqual(solution.decrypt([5, 7, 1, 4], 3), [12, 10, 16, 13])
        self.assertEqual(solution.decrypt([1, 2, 3, 4], 0), [0, 0, 0, 0])
        self.assertEqual(solution.decrypt([2, 4, 9, 3], -2), [12, 5, 6, 13])


if __name__ == "__main__":
    unittest.main()
