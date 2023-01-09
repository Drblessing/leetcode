class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Iterate through colors
        # 2. Keep a red and blue pointer to insert blue and red colors

        # 2.
        red, blue = 0, len(nums) - 1
        # 1.
        for i, v in enumerate(nums):
            if v == 0:
                nums[red], nums[i] = nums[i], nums[red]
                red += 1

        # Backward pass for 2
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                nums[blue], nums[i] = nums[i], nums[blue]
                blue -= 1
