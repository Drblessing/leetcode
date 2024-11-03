class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """Check if a string can be rotated to match another string."""

        if len(s) != len(goal):
            return False

        return goal in s + s
