class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Iterative
        # From statistics, we know a list of length n
        # has 2**n subsets.
        # We turn the numbers [0,2**n-1] into binary.
        # A 1 in binary includes the item, a 0 does not.
        # 1. Calculate total number of subsetes
        # 2. Iterate through each one
        # 3. Use binary to choose included elements of set

        subset_list = []
        # Iterate over each subset
        for i in range(2 ** len(nums)):
            # Binary
            binary_set = bin(i)[2:]
            # Format binary number to correct length
            if len(binary_set) < len(nums):
                binary_set = (len(nums) - len(binary_set)) * "0" + binary_set
            # Use binary number to include items
            subset = []
            for i, v in enumerate(binary_set):
                if v == "1":
                    subset.append(nums[i])
            # Add it to the list
            subset_list.append(subset)
        return subset_list
