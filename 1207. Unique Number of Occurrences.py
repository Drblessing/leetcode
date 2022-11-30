class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Count all elements in arr
        c = Counter(arr)
        occur = c.values()
        # Check the values in occur are all unique
        if len(occur) == len(set(occur)):
            return True
        return False
