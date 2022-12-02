class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check same length
        if len(word1) != len(word2):
            return False

        # Count letter occurences
        c1 = Counter(word1)
        c2 = Counter(word2)

        # Check same letters
        if set(c1) != set(c2):
            return False

        # Since letter frequencies are arbitrarily interchangable
        # all we care about now are that the frequencies are equal
        word1_frequencies = Counter(c1.values())
        word2_frequencies = Counter(c2.values())
        if word1_frequencies != word2_frequencies:
            return False

        # Equal lengths, letter, and frequences
        # means the strings are close
        return True
