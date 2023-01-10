class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1. Pop off first row
        # 2. Turn matrix counter clockwise
        # 3. Repeat until empty
        spiral = []
        while matrix:
            spiral.extend(matrix[0])
            matrix.pop(0)
            if not matrix:
                break
            r, c = len(matrix), len(matrix[0])
            new_matrix = []
            for col in range(c):
                new_row = []
                for row in range(r):
                    new_row.append(matrix[row][col])
                new_matrix.append(new_row)
            matrix = new_matrix[::-1]

        return spiral
