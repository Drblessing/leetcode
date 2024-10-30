from collections import deque
import unittest


class Solution:
    # The three possible directions for the next column.
    dirs = [-1, 0, 1]

    def maxMoves(self, grid):
        M, N = len(grid), len(grid[0])

        q = deque()
        vis = [[False] * N for _ in range(M)]

        # Enqueue the cells in the first column.
        for i in range(M):
            vis[i][0] = True
            q.append((i, 0, 0))

        max_moves = 0
        while q:
            sz = len(q)

            for _ in range(sz):
                row, col, count = q.popleft()

                # Update the maximum moves made so far.
                max_moves = max(max_moves, count)

                for dir in self.dirs:
                    # Next cell after the move.
                    new_row, new_col = row + dir, col + 1

                    # If the next cell isn't visited yet and is greater than
                    # the current cell value, add it to the queue with the
                    # incremented move count.
                    if (
                        0 <= new_row < M
                        and 0 <= new_col < N
                        and not vis[new_row][new_col]
                        and grid[row][col] < grid[new_row][new_col]
                    ):
                        vis[new_row][new_col] = True
                        q.append((new_row, new_col, count + 1))

        return max_moves


# Test cases
# grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# output = 3
# grid = [[3,2,4],[2,1,9],[1,1,7]]
# output = 0
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
        expected = 3
        self.assertEqual(self.solution.maxMoves(grid), expected)

    def test_case_2(self):
        grid = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
        expected = 0
        self.assertEqual(self.solution.maxMoves(grid), expected)

    def test_dummy(self):
        # Assert 2 == 2
        self.assertEqual(2, 2)


if __name__ == "__main__":
    grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
    print(Solution().maxMoves(grid))  # Output: 3
    grid = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
    print(Solution().maxMoves(grid))  # Output: 0
