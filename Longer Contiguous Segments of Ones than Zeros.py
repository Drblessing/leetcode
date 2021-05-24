class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count = [0, 0]

        for k, grp in itertools.groupby(s):
            k = int(k)
            count[k] = max(count[k], len(list(grp)))

        return count[1] > count[0]