# super easy in python
# the trick is to notice that every number is binary so we need
# at minimum the highest digit in the number

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)