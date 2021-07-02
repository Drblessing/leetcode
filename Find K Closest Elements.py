from operator import itemgetter


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = [(abs(i - x), i) for i in arr]

        i = sorted(i, key=itemgetter(0, 1))

        return sorted([i[1] for i in i[:k]])

