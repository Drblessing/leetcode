class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i, v in enumerate(nums):

            # target - v1 = v2
            if target - v in d: return d[target - v], i
            d[v] = i

            # return none by default if not found