from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        """Reverse the string inside paranthesis recurisvely starting
        with the innermost."""

        stack = deque()
        for l in s:
            if l == "(":
                stack.append(l)

            elif l == ")":
                # pop from stack until we find the matching "("
                substring = ""
                while stack[-1] != "(":
                    substring += stack.pop()
                # pop "("
                stack.pop()
                # reverse string and append
                stack.extend(reversed(substring))
            else:
                stack.append(l)

        print(stack)
        return "yo"
