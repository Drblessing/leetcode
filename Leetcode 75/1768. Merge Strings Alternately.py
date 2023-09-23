class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Merge words alternately."""

        # Initialize empty string.
        merged = ""

        while word1 and word2:
            # Add first letter of word1.
            merged += word1[0]
            # Remove first letter of word1.
            word1 = word1[1:]

            # Add first letter of word2.
            merged += word2[0]
            # Remove first letter of word2.
            word2 = word2[1:]

        # Add remaining letters.
        merged += word1 + word2

        return merged


word1 = "abc"
word2 = "pqr"

if __name__ == "__main__":
    print(Solution().mergeAlternately(word1, word2))
