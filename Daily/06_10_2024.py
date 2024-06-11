from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c1 = Counter(arr1)

        ans = []
        for num in arr2:
            ans += [num] * c1[num]
            c1.pop(num)

        for num in sorted(c1.keys()):
            ans += [num] * c1[num]

        return ans
