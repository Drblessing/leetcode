class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1. Iterate through nums
        # 2. Add num to hashset
        # 3. Check if num already in hashset

        # 1.
        seen = set()
        for num in nums:
            # 3.
            if num in seen:
                return True
            else:
                # 2.
                seen.add(num)
        return False
