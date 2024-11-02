class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """Check if a sentence is circular.
        A sentence is cricular if the last letter of each word is the same
        as the first letter of the next word.
        """
        if not sentence:
            return False

        n = len(sentence)
        for i, v in enumerate(sentence):
            if v == " ":
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        return sentence[-1] == sentence[0]
