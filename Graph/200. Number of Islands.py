class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        # 1. Iterate through grid
        # 2. Keep track of visited
        # 3. Visit adjacent spaces to islands

        visited = set()
        return sum(
            self._dfs(grid, i, j, visited)
            for i in range(len(grid))
            for j in range(len(grid[0]))
        )

    def _dfs(self, grid: List[List[str]], row: int, col: int, visited: set) -> None:

        if not (
            0 <= row < len(grid)
            and 0 <= col < len(grid[0])
            and (row, col) not in visited
            and grid[row][col] == "1"
        ):
            return 0

        visited.add((row, col))

        self._dfs(grid, row + 1, col, visited)
        self._dfs(grid, row - 1, col, visited)
        self._dfs(grid, row, col + 1, visited)
        self._dfs(grid, row, col - 1, visited)

        return 1
