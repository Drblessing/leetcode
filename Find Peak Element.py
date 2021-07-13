class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            # Handle nums of len 1 or 2
            if i + 1 == len(nums): return i

            if nums[i] > nums[i + 1]: return i



