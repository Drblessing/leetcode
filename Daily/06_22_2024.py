class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize variables
        odd_count = 0  # Running count of odd numbers
        result = 0  # Total number of valid subarrays
        count_map = {0: 1}  # Hash map to store counts of odd number sums

        for num in nums:
            # Increment odd_count if the number is odd
            if num % 2 == 1:
                odd_count += 1

            # If we've seen (odd_count - k) before, it means we've found valid subarrays
            if odd_count - k in count_map:
                result += count_map[odd_count - k]

            # Update the count for the current odd_count
            count_map[odd_count] = count_map.get(odd_count, 0) + 1

        return result
