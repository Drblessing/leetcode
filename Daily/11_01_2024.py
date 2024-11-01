import unittest


class Solution:
    def makeFancyString(self, s: str) -> str:
        """Delete the minimum number of characters to make s fancy.
        A string s is fancy if there are no three consecutive equal characters.
        """

        # Check length of the string
        if len(s) <= 2:
            return s

        elif len(s) == 3:
            if s[0] == s[1] == s[2]:
                return s[:2]
            else:
                return s

        output = s[0]
        # Iterate through the middle cahracters of the string
        for i in range(1, len(s) - 1):
            if s[i] == s[i - 1] == s[i + 1]:
                continue
            output += s[i]
        return output + s[-1]


# "leeetcode" -> "leetcode"
# "aaabaaaa" -> "aabaa"
# "aab" -> "aab"


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_make_fancy_string(self):
        self.assertEqual(self.solution.makeFancyString("leeetcode"), "leetcode")
        self.assertEqual(self.solution.makeFancyString("aaabaaaa"), "aabaa")
        self.assertEqual(self.solution.makeFancyString("aab"), "aab")


if __name__ == "__main__":
    unittest.main(verbosity=2)
