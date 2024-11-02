from typing import List
import unittest
import itertools


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """Defuse the bomb by decrypting the code.
        k is the decryption key.
        If k > 0, replace the ith number with the sum of the next k numbers.
        If k < 0, replace the ith number with the sum of the previous k numbers.
        If k == 0, replace the ith number with 0.
        -(n-1) <= k <= n - 1
        The code is a circular array of length n.
        """

        n = len(code)

        # If k is 0 return a list of n zeros.
        if k == 0:
            return [0] * n

        # Prepend/append the code to itself k times to handle circularity.
        if k > 0:
            code = code + code[:k]
        else:
            code = code[k:] + code

        # Initialize the result list.
        res = []

        # Handle the case when k is positive.
        if k > 0:
            for i in range(n):
                res.append(sum(code[i + 1 : i + 1 + k]))
        # Handle the case when k is negative.
        else:
            for i in range(n):
                res.append(sum(code[i : i - k]))

        return res


# Test cases
# Input: code = [5, 7, 1, 4], k = 3
# Output: [12, 10, 16, 13]
# Input: code = [1, 2, 3, 4], k = 0
# Output: [0, 0, 0, 0]
# Input: code = [2, 4, 9, 3], k = -2
# Output: [12, 5, 6, 13]
class Test(unittest.TestCase):
    def test_decrypt(self):
        solution = Solution()
        self.assertEqual(solution.decrypt([5, 7, 1, 4], 3), [12, 10, 16, 13])
        self.assertEqual(solution.decrypt([1, 2, 3, 4], 0), [0, 0, 0, 0])
        self.assertEqual(solution.decrypt([2, 4, 9, 3], -2), [12, 5, 6, 13])


if __name__ == "__main__":
    unittest.main()
