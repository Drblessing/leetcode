class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        n = len(grid)

        return sum(self._dfs(grid, i, j, visited)
                   for i in range(n)
                   for j in range(n))

    def _dfs(self, grid: List[List[str]], row: int, col: int, visited: set) -> None:

        if (row, col) in visited or grid[row][col] == '0': return 0

        visited.add((row, col))

        if grid[row][col] == 1:
            for new_col in range(len(grid)):
                self._dfs(grid, col, new_col, visited)

        return 1
