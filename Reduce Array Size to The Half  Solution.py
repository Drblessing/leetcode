from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l = len(arr)
        target_size = len(arr) // 2
        c = Counter(arr).most_common()
        s = 0

        while l > target_size:
            s += 1
            removed_integer = c.pop(0)

            l -= removed_integer[1]

        return s
