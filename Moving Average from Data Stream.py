from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = size
        self.l = 0
        self.sum = 0

    def next(self, val: int) -> float:

        if self.l < self.size:
            self.queue.append(val)
            self.sum += val
            self.l += 1

        else:
            self.sum -= self.queue.popleft()
            self.sum += val
            self.queue.append(val)

        return self.sum / self.l

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)