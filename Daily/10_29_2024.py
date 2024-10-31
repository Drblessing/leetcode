from collections import deque
import unittest


class Solution:
    # Directions to move in the grid
    directions = [-1, 0, 1]

    def maxMoves(self, grid):
        """Calculate the maximum number of moves possible in a grid.
        Only moving right, down, or diagonally is allowed, where the integer is increasing.
        The grid is a square matrix of integers.
        You have to start in the first column, any row."""

        # Get the rows and columns of the grid
        m, n = len(grid), len(grid[0])
        # m is the number of rows, n is the number of columns

        # Visited set to keep track of visited cells
        visited = [[False] * n for _ in range(m)]

        # Queue to keep track of the cells to visit
        queue = deque()

        # Add the starting cells to the queue
        for i in range(m):
            queue.append((i, 0, 0))
            visited[i][0] = True

        # Initialize the maximum moves to 0
        max_moves = 0

        # BFS
        while queue:
            # Get the current cell
            i, j, moves = queue.popleft()

            # Get the new maximum moves
            max_moves = max(max_moves, moves)

            # Check the neighbors
            for d in self.directions:
                # Col always increases by 1
                # Row increases by d
                new_i, new_j = i + d, j + 1

                # Check if the new cell is within bounds,
                # and if it has not been visited
                # and if the new cell is greater than the current cell
                if (
                    0 <= new_i < m
                    and 0 <= new_j < n
                    and not visited[new_i][new_j]
                    and grid[new_i][new_j] > grid[i][j]
                ):
                    # Mark the new cell as visited before enqueueing because
                    # we don't want to visit the same cell multiple times
                    visited[new_i][new_j] = True

                    # Add the new cell to the queue
                    queue.append((new_i, new_j, moves + 1))

        return max_moves

    # Time complexity: O(m * n)
    # Space complexity: O(m * n)


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
