import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create a formatter and set the formatter for the handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        """Find the maximum number of children that can be satisfied.

        g: list[int] -> List of greed factors
        s: list[int] -> List of cookie sizes
        return: int -> The maximum number of children that can be satisfied
        """
        logger.debug(f"Executing findContentChildren\nwith g: {g} and s: {s}")

        # Error handling
        if not g:
            raise ValueError("The children list cannot be empty.")

        # Sort the lists
        g.sort()
        s.sort()

        # Initialize the counters
        c = 0
        i = 0

        # Loop through the cookies and children
        while i < len(s) and c < len(g):

            # The current cookie can satisfy the current child
            # We go from the least greedy child to the most greedy child
            if s[i] >= g[c]:
                c += 1

            # Check the next cookie
            i += 1

        logger.debug(f"Returning {c}")
        return c


Solution().findContentChildren([1, 2, 3], [1, 1])

# Test
import pytest


# Define the tests
def test_findContentChildren():
    solution = Solution()

    assert solution.findContentChildren([1, 2, 3], [1, 1]) == 1
    assert solution.findContentChildren([1, 2], [1, 2, 3]) == 2
    assert solution.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]) == 4
    assert solution.findContentChildren([1, 2, 3], []) == 0
    assert solution.findContentChildren([], [1, 2, 3]) == 0

    with pytest.raises(ValueError):
        solution.findContentChildren([], [])


# Run the tests
# pytest.main()
