import unittest
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
                stack.extend(substring)
            else:
                stack.append(l)

        return "".join(stack)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverseParentheses(self):
        self.assertEqual(self.solution.reverseParentheses("(abcd)"), "dcba")
        self.assertEqual(self.solution.reverseParentheses("(u(love)i)"), "iloveu")
        self.assertEqual(self.solution.reverseParentheses("(ed(et(oc))el)"), "leetcode")
        self.assertEqual(
            self.solution.reverseParentheses("a(bcdefghijkl(mno)p)q"),
            "apmnolkjihgfedcbq",
        )


if __name__ == "__main__":
    pass
    unittest.main()
