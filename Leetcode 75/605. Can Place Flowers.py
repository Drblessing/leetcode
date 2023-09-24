class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Determine if flowers are placeable."""

        # Check if no flower needs to be planted.
        if n == 0:
            return True

        # Initialize counter of number of flowers we can plant.
        count = 0
        # Iterate through flowerbed.
        for i in range(len(flowerbed)):
            # Check for any empty plot.
            if flowerbed[i] == 0:
                # Check for empty left and right plots.
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # Add to count if eligble.
                if left_empty and right_empty:
                    count += 1
                    # Check for completion.
                    if count >= n:
                        return True
                    # Plant flower.
                    flowerbed[i] = 1
        # No eligble configuration.
        return False
