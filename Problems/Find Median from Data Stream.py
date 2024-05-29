from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:

        heappush(self.hi, -heappushpop(self.lo, -num))

        if len(self.lo) < len(self.hi):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self) -> float:

        if len(self.hi) < len(self.lo): return -self.lo[0]

        return (self.hi[0] - self.lo[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()