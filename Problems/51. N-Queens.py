from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = [-1] * n  # board[i] = column index of queen in row i, -1 if none placed

        def safe(row, col):
            for r in range(row):
                c = board[r]
                if c == col or abs(c - col) == abs(r - row):
                    return False
            return True

        def backtrack(row):
            if row == n:
                # All queens placed, convert to solution format
                solution = []
                for r in range(n):
                    line = ["."] * n
                    line[board[r]] = "Q"
                    solution.append("".join(line))
                solutions.append(solution)
                return

            for col in range(n):
                if safe(row, col):
                    board[row] = col
                    backtrack(row + 1)
                    # No need to "remove" col explicitly since we'll overwrite later

        backtrack(0)
        return solutions


Solution().solveNQueens(4)
