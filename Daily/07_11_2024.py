import unittest
from collections import deque


class Solution:

    def reverseParentheses(self, s: str) -> str:
        """Reverse the string inside paranthesis recurisvely starting
        with the innermost. Utilize the wormhole teleportation technique to reverse the string.
        """
        n = len(s)
        teleportation_map = []
        pair_map = [0] * n
        # pair up the paranthesis
        for i, l in enumerate(s):
            if l == "(":
                teleportation_map.append(i)
            elif l == ")":
                j = teleportation_map.pop()
                pair_map[i], pair_map[j] = j, i
        # Second pass, teleport around the string
        i, d = 0, 1
        result = []
        while i < n:
            if s[i] in "()":
                i = pair_map[i]
                d = -d
            else:
                result.append(s[i])
            i += d

        return "".join(result)


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
