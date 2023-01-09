class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Iterate through sorted intervals
        # 2. Check if end is bigger than next start
        # 3. If true, merge interval in place and delete next interval

        # Sort intervals first to fix algorithm
        intervals.sort(key=lambda x: x[0])
        # 1.
        i = 0
        while i < len(intervals) - 1:
            cur_start, cur_end = intervals[i]
            # 2.
            if cur_end >= intervals[i + 1][0]:
                # 3.
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals[i][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals.pop(i + 1)
            else:
                i += 1

        return intervals
