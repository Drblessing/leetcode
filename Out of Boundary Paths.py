from functools import lru_cache


class Solution:

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @lru_cache(None)
        def _dp(row: int = startRow, col: int = startColumn, moves: int = maxMove):

            if row < 0 or row >= m or col < 0 or col >= n:
                return int(moves >= 0)

            elif moves < 0:
                return 0

            res = 0

            res += _dp(row + 1, col, moves - 1)
            res += _dp(row - 1, col, moves - 1)
            res += _dp(row, col + 1, moves - 1)
            res += _dp(row, col - 1, moves - 1)

            return res

        return _dp() % (10 ** 9 + 7)



