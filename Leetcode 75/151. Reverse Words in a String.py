class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse words in a string."""

        # Split string into words.
        words = s.split()

        # Reverse words.
        s = reversed(words)

        # Join with spaces.
        return " ".join(s)
