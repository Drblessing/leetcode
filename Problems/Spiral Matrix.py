class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        while matrix:
            ans += matrix.pop(0)

            # Rotate
            matrix = list(zip(*matrix))[::-1]

        return ans
