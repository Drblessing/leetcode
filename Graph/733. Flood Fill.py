class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # Recursion
        # 1. Change pixel
        # 2. Run on every connecting pixel
        # 3. If diff, change pixel
        # 4. If same, stop

        # Recursive depth first
        starting_color = image[sr][sc]
        if color == starting_color:
            return image
        self.recursiveFlood(image, sr, sc, color, starting_color)
        return image

    def recursiveFlood(self, image, row, col, color, starting_color):
        # Do nothing
        if image[row][col] != starting_color:
            return

        else:
            # Check every direction
            image[row][col] = color
            for direction in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                horizontal, vertical = direction
                new_row, new_col = row + horizontal, col + vertical

                if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]):
                    self.recursiveFlood(image, new_row, new_col, color, starting_color)
