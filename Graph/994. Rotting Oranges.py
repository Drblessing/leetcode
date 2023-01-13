class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        # 1. Iterate through grid
        # 2. If rotten orange, spread through oranges
        # 3. Keep track of minutes
        # 4. Return highest minute if no fresh oranges

        # Rows and cols
        m, n = len(grid), len(grid[0])
        minutes_passed = 0
        fresh_count = 0

        # Queue for rotting
        rotting = deque()

        # Find fresh and rotting
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rotting.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # While rotting and still fresh oranges
        while rotting and fresh_count > 0:

            # Safe to increment minutes because we process on level at a time
            minutes_passed += 1

            for _ in range(len(rotting)):
                x, y = rotting.popleft()

                # Rot all oranges next to it
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    # Check in bounds and fresh orange
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        # Rot orange
                        grid[new_x][new_y] = 2
                        fresh_count -= 1
                        # Add it to stack
                        rotting.append((new_x, new_y))

        return -1 if fresh_count else minutes_passed
