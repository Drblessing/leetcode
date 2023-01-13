class Solution:
    def exist(self, board, word):
        # DFS
        # 1. Iterate through grid in DFS
        # 2. Check each direction
        # 3. Mark visited for each search tree
        # 4. Mark unvisited after backtracking

        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if self.dfs(row, col, board, word, rows, cols):
                    return True
        return False

    def dfs(self, row, col, board, word, rows, cols):
        # Word found
        if len(word) == 0:
            return True

        # Wrong letter or out of bounds
        if not (0 <= row < rows and 0 <= col < cols) or board[row][col] != word[0]:
            return False
        # It's the right letter
        # Mark letter visited temporarily
        board[row][col] = "#"

        # Check each direction
        res = (
            self.dfs(row + 1, col, board, word[1:], rows, cols)
            or self.dfs(row - 1, col, board, word[1:], rows, cols)
            or self.dfs(row, col + 1, board, word[1:], rows, cols)
            or self.dfs(row, col - 1, board, word[1:], rows, cols)
        )

        # Mark letter not visited for other paths
        board[row][col] = word[0]
        return res
