import bisect


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # Combine difficulty and profit, and sort by difficulty
        jobs = sorted(zip(difficulty, profit))

        # Create a sorted list of unique difficulties and corresponding max profits
        max_profit_at_difficulty = []
        max_profit = 0
        for d, p in jobs:
            max_profit = max(max_profit, p)
            max_profit_at_difficulty.append((d, max_profit))

        # Extract difficulties and max profits into separate lists for bisect
        difficulties, max_profits = zip(*max_profit_at_difficulty)

        # Calculate the total profit
        total_profit = 0

        for w in worker:
            # Find the rightmost difficulty that is less than or equal to the worker's ability
            idx = bisect.bisect_right(difficulties, w) - 1
            if idx >= 0:
                total_profit += max_profits[idx]

        return total_profit
