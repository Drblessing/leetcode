class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # BFS
        rows, cols = len(maze), len(maze[0])

        # Set visited spaces to "+"
        maze[entrance[0]][entrance[1]] = "+"

        # Process stops in a queue
        queue = collections.deque()
        # Add first stop in queue
        queue.appendleft([entrance[0], entrance[1], 0])

        # Iterate until queue empty or we reach an exit
        while queue:
            row, col, steps = queue.pop()

            # Check each direction breadth first
            for r, c in [
                [row + 1, col],
                [row - 1, col],
                [row, col + 1],
                [row, col - 1],
            ]:
                # Check in bounds and it not a wall
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == ".":
                    # Check for exit
                    if (r == 0) or (c == 0) or (r == rows - 1) or (c == cols - 1):
                        return steps + 1
                    # Add stop to visited
                    maze[r][c] = "+"

                    # BFS, new stops get added at the end of the queue, not the front
                    queue.appendleft([r, c, steps + 1])
        # No exit found
        return -1
