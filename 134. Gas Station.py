class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy solution
        # Always pick the optimal starting spot
        #
        # Solution
        # 1. Keep track of current and trip tank
        # 2. Find optimal starting point because unique starting
        # 3. Calculate current and trip tank

        trip_tank, cur_tank, start, n = 0, 0, 0, len(gas)

        for i in range(n):
            trip_tank += gas[i] - cost[i]
            cur_tank += gas[i] - cost[i]

            if cur_tank < 0:
                start = i + 1
                cur_tank = 0

        return start if trip_tank >= 0 else -1
