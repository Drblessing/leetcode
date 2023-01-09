class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Remove uppercase, non-alpha num
        # 2. Two pointers front and back
        # 3. Iterate pointers checking for same letter

        # 1.
        s = "".join([letter.lower() for letter in s if letter.isalnum()])
        # 2.
        l, r = 0, len(s) - 1
        # 3.
        while l <= r:
            # Not a palindrome
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
