class Solution:
    def isValid(self, s: str) -> bool:
        # Stack
        # 1. Iterate through s
        # 2. Add letters to stack
        # 3. Check if letters match

        # Create key
        key = {")": "(", "}": "{", "]": "["}

        stack = []
        for letter in s:
            # Lookup
            if letter in key:
                match = key[letter]
                # Make sure stack matches
                if not stack or match != stack.pop():
                    return False

            else:
                stack.append(letter)
        # Stack must be empty
        return len(stack) == 0
