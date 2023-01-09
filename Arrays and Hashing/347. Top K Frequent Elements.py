class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We use a hashmap to do a single pass through the
        # nums, keeping track of the kth most prevalent as we go through
        # We could also use a counter built-in data structure

        # Solution
        # 1. Iterate through nums
        # 2. Increment hashmap for num
        # 3. Keep track of kth most common

        return [i[0] for i in Counter(nums).most_common(k)]
