from typing import Iterator
import unittest


class Solution:
    BASE = 26

    @staticmethod
    def letter_to_number(letter: str) -> int:
        """Convert a single letter to its corresponding number."""
        if not letter.isalpha() or len(letter) != 1:
            raise ValueError(
                f"Invalid input: {letter}. Expected a single alphabetic character."
            )
        return ord(letter.upper()) - ord("A") + 1

    @staticmethod
    def is_uppercase_letters(s: str) -> bool:
        return s.isupper() and s.isalpha()

    @staticmethod
    def string_to_numbers(letters: str) -> Iterator[int]:
        """Convert a string of letters to an iterator of corresponding numbers."""
        return map(Solution.letter_to_number, letters)

    def titleToNumber(self, column_title: str) -> int:
        """
        Convert an Excel column title to its corresponding column number.

        Args:
            column_title (str): The Excel column title (e.g., 'A', 'B', 'C', ..., 'Z', 'AA', 'AB', ...)

        Returns:
            int: The corresponding column number

        Raises:
            ValueError: If the input contains non-alphabetic characters
        """
        if not column_title:
            raise ValueError("Invalid column title: Empty string.")
        if not Solution.is_uppercase_letters(column_title):
            raise ValueError(
                f"Invalid column title: {column_title}. Title should contain only alphabetic characters."
            )

        n = len(column_title)

        return sum(
            num * (Solution.BASE ** (n - i - 1))
            for i, num in enumerate((Solution.string_to_numbers(column_title)))
        )


# Unit Test
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simples_cases(self):
        self.assertEqual(self.solution.titleToNumber("A"), 1)
        self.assertEqual(self.solution.titleToNumber("AB"), 28)
        self.assertEqual(self.solution.titleToNumber("ZY"), 701)

    def test_letter_to_number(self):
        self.assertEqual(Solution.letter_to_number("A"), 1)
        self.assertEqual(Solution.letter_to_number("Z"), 26)
        self.assertEqual(Solution.letter_to_number("a"), 1)
        self.assertEqual(Solution.letter_to_number("z"), 26)

        with self.assertRaises(ValueError):
            Solution.letter_to_number("AA")
        with self.assertRaises(ValueError):
            Solution.letter_to_number("1")
        with self.assertRaises(ValueError):
            Solution.letter_to_number("")

    def test_is_uppercase_letters(self):
        self.assertTrue(Solution.is_uppercase_letters("A"))
        self.assertTrue(Solution.is_uppercase_letters("ABC"))
        self.assertFalse(Solution.is_uppercase_letters("abc"))
        self.assertFalse(Solution.is_uppercase_letters("A1C"))
        self.assertFalse(Solution.is_uppercase_letters(""))

    def test_string_to_numbers(self):
        self.assertEqual(list(Solution.string_to_numbers("ABC")), [1, 2, 3])
        self.assertEqual(list(Solution.string_to_numbers("ZYX")), [26, 25, 24])

        with self.assertRaises(ValueError):
            list(Solution.string_to_numbers("A1C"))

    def test_titleToNumber(self):
        test_cases = [
            ("A", 1),
            ("B", 2),
            ("Z", 26),
            ("AA", 27),
            ("AB", 28),
            ("ZY", 701),
            ("AAA", 703),
            ("FXSHRXW", 2147483647),
        ]

        for title, expected in test_cases:
            with self.subTest(title=title):
                self.assertEqual(self.solution.titleToNumber(title), expected)

    def test_titleToNumber_edge_cases(self):
        with self.assertRaises(ValueError):
            self.solution.titleToNumber("")
        with self.assertRaises(ValueError):
            self.solution.titleToNumber("A1")
        with self.assertRaises(ValueError):
            self.solution.titleToNumber("a")


if __name__ == "__main__":
    unittest.main()
