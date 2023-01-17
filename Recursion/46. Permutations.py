class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Recursive
        # 1. Call itself with one letter added
        # 2. Recursive until no letters left

        # Store all permutations
        permutations = []

        def recursive(nums, permutation=[]):
            # Found a permutation
            if len(nums) == 0:
                # Add it to the answer
                permutations.append(permutation)
            # Go through remaining letters
            for i in range(len(nums)):
                # Add one letter to permutation
                # and removce it from next recursive call
                recursive(nums[:i] + nums[i + 1 :], permutation + [nums[i]])

        recursive(nums)
        return permutations
