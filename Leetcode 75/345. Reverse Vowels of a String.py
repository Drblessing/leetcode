class Solution:
    def reverseVowels(self, s: str) -> str:
        """Reverse only the vowels in a string."""

        # Initialize vowels set.
        vowels = set("aeiouAEIOU")

        # Convert string into list to allow for reassignment
        s = list(s)

        # Initalize pointers.
        l, r = 0, len(s) - 1

        # Iterate through the string.
        # Iterate pointers until they hit a vowel,
        # or they go past each other.
        while l < r:
            while s[l] not in vowels and l < r:
                l += 1
            while s[r] not in vowels and l < r:
                r -= 1
            # If no vowels will swap the same letter.
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        # Return string.
        return "".join(s)
