from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        c = Counter(arr).most_common()

        target_len = len(arr) // 2

        count = 0

        for i in range(len(c)):

            count += c[i][1]

            if count >= target_len: return i + 1

