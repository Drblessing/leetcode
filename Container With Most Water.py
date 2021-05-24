class Solution:
    def maxArea(self, height: List[int]) -> int:

        # init left and right pointers
        size = len(height)

        l, r = 0, size - 1

        area = 0

        max_width = size - 1

        # iterate through all possible widhts
        for width in range(max_width, 0, -1):

            # calculate area passed on shorter height
            area = max(area, width * min(height[l], height[r]))

            # remove shorter height from container because we've found it's max area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area