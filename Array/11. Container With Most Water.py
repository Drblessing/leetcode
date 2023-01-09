class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Calcualte area for each width, using the best possible
        # lines
        # 1. Iterate from potential widths
        # 2. Change smaller line
        max_width = len(height) - 1
        l, r = 0, len(height) - 1
        area = 0
        # 1.
        for w in range(max_width, 0, -1):
            # Calcualte max area
            area = max(area, w * min(height[l], height[r]))
            # Change smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area
