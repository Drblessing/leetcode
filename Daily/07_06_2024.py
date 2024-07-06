class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """Calculate where the pillow is."""

        # We must divide n by time.
        # If the quotient is an even number, we go from the start,
        # if the quotient is an odd number, we go in the reverse.

        # Then the remainder determiens the position
        quotient = time // (n - 1)
        remainder = time % (n - 1)

        if quotient % 2 == 0:
            return remainder + 1

        else:
            return n - remainder
