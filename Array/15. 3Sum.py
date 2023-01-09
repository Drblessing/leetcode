class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Sort nums
        # 2. Iterate through nums
        # 3. Use converging search to find potential threeSums

        # 1.
        nums.sort()
        ans = set()
        # 2.
        for left in range(len(nums) - 2):
            # Skip repeat numbers to save computation
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            # 3.
            mid = left + 1
            right = len(nums) - 1

            while mid < right:

                s = nums[left] + nums[mid] + nums[right]

                # Sum too high
                # decrease sum
                if s > 0:
                    right -= 1

                # Sum too low
                # increase
                elif s < 0:
                    mid += 1
                # Sum found
                # keep searching
                else:
                    ans.add((nums[left], nums[mid], nums[right]))
                    mid += 1
                    right -= 1

        return ans
