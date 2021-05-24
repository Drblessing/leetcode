# 100% memory!

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # init area
        area = 0

        # check each width, blasting the shorter height from existence
        for w in range(len(height) - 1, 0, -1):

            area = max(area, w * min(height[0], height[-1]))

            if height[0] < height[-1]:
                height.pop(0)
            else:
                height.pop()

        return area