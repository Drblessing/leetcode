from collections import Counter  # performance Counter


class Solution:
    def maxProduct(self, words: List[str]) -> int:

        n = len(words)

        words_c = [set(w) for w in words]

        p = 0

        for i in range(n):

            for j in range(n):

                if words_c[i].intersection(words_c[j]) == set():
                    p = max(p, len(words[i]) * len(words[j]))

        return p


