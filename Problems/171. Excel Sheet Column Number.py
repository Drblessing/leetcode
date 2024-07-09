from typing import Iterator


class Solution:
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
            num * (26 ** (n - i - 1))
            for i, num in enumerate((Solution.string_to_numbers(column_title)))
        )
