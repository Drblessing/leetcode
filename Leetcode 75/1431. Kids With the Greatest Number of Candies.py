class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """Find the kids that will have the greatest number of candies after adding extraCandies."""
        # Find the max number of candies.
        max_candies = max(candies)
        # Return a list of booleans.
        return [candy + extraCandies >= max_candies for candy in candies]
