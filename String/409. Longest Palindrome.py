class Solution:
    def longestPalindrome(self, s: str) -> int:
        # To build a palindrome
        # we need even numbers of letter
        # and can also throw in a singlet in the middle
        # 1. Count the letters in s
        # 2. Cound number of pairs in s
        # 3. Add 1 if a letter is remaining

        longest = 0
        singlet = False
        for letter, amount in Counter(s).items():
            # Pairs
            if amount % 2 == 0:
                longest += amount
            # Left over
            else:
                # Put letter in the middle if space
                if not singlet:
                    longest += 1
                    singlet = True
                # Add remaining pairs
                longest += amount - 1
        return longest
