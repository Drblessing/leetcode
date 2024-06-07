class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        """Find the maximum number of children that can be satisfied.

        g: list[int] -> List of greed factors
        s: list[int] -> List of cookie sizes
        return: int -> The maximum number of children that can be satisfied
        """

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

        return c
