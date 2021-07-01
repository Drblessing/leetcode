from statistics import median


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        self.l = 0

    def addNum(self, num: int) -> None:
        self.queue.append(num)
        self.queue.sort()
        self.l += 1

    def findMedian(self) -> float:
        # Odd # of numbers in the data stream.
        if self.l % 2 == 1:
            return self.queue[self.l // 2]

        # Even # of numbers

        n1, n2 = self.queue[self.l // 2], self.queue[self.l // 2 - 1]

        return (n1 + n2) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()