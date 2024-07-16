class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """Return if increaseing triplet subsequence exists."""

        # Initialize smallest and second_smallet to inf.
        smallest = second_smallest = float("inf")

        # Iterate through nums.
        for num in nums:
            # Check for new smallest.
            if num <= smallest:
                smallest = num
            # Check for second smallest.
            elif num <= second_smallest:
                second_smallest = num
            # Number is bigger than both smallest and second smallest.
            # Valid triplet.
            else:
                return True
        # No valid triplet
        return False
