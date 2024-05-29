class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        merged = []

        for i in sorted(intervals, key=lambda x: x[0]):

            # Init answer with first interval
            if not merged: merged.append(i)

            # No collision in intervals
            if merged[-1][-1] < i[0]:
                merged.append(i)

            # Collision in intervals
            else:

                # Update current interval with new ending
                merged[-1][-1] = max(merged[-1][-1], i[1])

        return merged
