class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. Init hashmap
        # 2. Iterate through nums
        # 3. Increment hashmap for each num
        # 4. When counter is over n /2, return num

        # 1.
        hashmap = defaultdict(int)
        threshold = len(nums) / 2
        # 2.
        for num in nums:
            # 3.
            hashmap[num] += 1
            # 4.
            if hashmap[num] > threshold:
                return num
