class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        d = {}

        for i, v in enumerate(order):
            d[v] = i

        for i, v in enumerate(words[:-1]):

            for j in range(len(words[i])):

                if j == len(words[i + 1]):
                    return False

                if d[words[i][j]] == d[words[i + 1][j]]:
                    continue

                elif d[words[i][j]] > d[words[i + 1][j]]:
                    return False

                elif d[words[i][j]] < d[words[i + 1][j]]:
                    break

        return True












 