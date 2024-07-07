class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """Calculate the total number of water bottles."""
        # Init data structures
        totalDrinks = 0
        emptyBottles = 0
        # Drink and return buttles until we're out
        while numBottles > 0:
            # Drink all the current bottles
            totalDrinks += numBottles
            emptyBottles += numBottles
            numBottles = 0
            # Return as many bottles as possible
            if emptyBottles >= numExchange:
                numBottles += emptyBottles // numExchange
                emptyBottles = emptyBottles % numExchange

        return totalDrinks
