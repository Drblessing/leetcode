class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution
        # 1. Iterate through nums, logging seen numbers
        # 2. If target - num in seen, return indices

        # 1.
        seen = {}
        for i, num in enumerate(nums):

            # 2.
            if target - num in seen:
                return [i, seen[target - num]]
            else:
                seen[num] = i
