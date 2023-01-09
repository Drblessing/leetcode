class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # 1. Iterate through the intervals
        # 2. Split intervals into left of new, and right of new
        # 3. If overlap, expand newInterval to largest merge

        ns, ne = newInterval
        l, r = [], []
        for s, e in intervals:
            if e < ns:
                l += [[s, e]]
            elif s > ne:
                r += [[s, e]]
            else:
                ns = min(s, ns)
                ne = max(e, ne)
        return l + [[ns, ne]] + r
