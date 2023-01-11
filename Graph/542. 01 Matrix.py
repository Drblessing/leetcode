class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS
        # 1. Visit every 0 and add to queue
        # 2. Process queue

        rows, cols = len(mat), len(mat[0])
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = -1

        while queue:
            row, col = queue.popleft()
            for direction_x, direction_y in directions:
                new_row, new_col = row + direction_x, col + direction_y

                if (0 <= new_row < rows and 0 <= new_col < cols) and mat[new_row][
                    new_col
                ] == -1:
                    mat[new_row][new_col] = mat[row][col] + 1
                    queue.append((new_row, new_col))
                else:
                    continue

        return mat
