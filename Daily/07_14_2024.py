from collections import Counter
from typing import List, Tuple


class Solution:

    @staticmethod
    def parse_chemical_symbol(formula: str, n: int) -> tuple:
        """Parse a chemical symbol and return the index
        after the symbol and it's string value,
        and its numeric value"""

        # Get symbol
        symbol = formula[n]
        n += 1
        while n < len(formula) and formula[n].islower():
            symbol += formula[n]
            n += 1

        # Get numeric value
        numeric_string = ""
        while n < len(formula) and formula[n].isdigit():
            numeric_string += formula[n]
            n += 1
        if not numeric_string:
            numeric_string = 1

        c = Counter()
        c[symbol] = int(numeric_string)

        # Turn counter into a string
        result_string = ""
        for key, value in c.items():
            result_string += key
            if value != 1:
                result_string += str(value)

        return result_string, n

    @staticmethod
    def parse_chemical_symbol_counter(formula: str, n: int) -> tuple:
        """Parse a chemical symbol and return the index
        after the symbol and it's string value,
        and its numeric value"""

        # Get symbol
        symbol = formula[n]
        n += 1
        while n < len(formula) and formula[n].islower():
            symbol += formula[n]
            n += 1

        # Get numeric value
        numeric_string = ""
        while n < len(formula) and formula[n].isdigit():
            numeric_string += formula[n]
            n += 1
        if not numeric_string:
            numeric_string = 1

        c = Counter()
        c[symbol] = int(numeric_string)

        return c, n

    @staticmethod
    def parse_non_paranthesis(fomula: str, n: int):
        """Parse a string that does not contain any paranthesis."""
        result = ""
        while n < len(fomula):
            if Solution.is_uppercase_letter(fomula[n]):
                r, n = Solution.parse_chemical_symbol(fomula, n)
                result += r
            else:
                n += 1
        return result, n

    @staticmethod
    def final_parse(formula: str):
        """Parse the final formula and return the count of atoms."""
        result = Counter()
        n = 0
        while n < len(formula):
            if Solution.is_uppercase_letter(formula[n]):
                r, n = Solution.parse_chemical_symbol_counter(formula, n)
                result += r

            else:
                n += 1
        return result

    @staticmethod
    def is_digit(char: str):
        """Check if a character is a digit."""
        return char.isdigit()

    @staticmethod
    def is_lowercase_letter(char: str):
        """ "Check if a chracter is a lowercase letter."""
        return char.islower()

    @staticmethod
    def is_uppercase_letter(char: str):
        """Check if a character is an uppercase letter."""
        return char.isupper()

    def countOfAtoms(self, formula: str) -> str:
        """Count the number of atoms in a formula."""

        stack = []
        n = 0
        # Replace parantehsis with a string
        while n < len(formula):
            if formula[n] == "(":
                stack.append(n)
                n += 1
            elif formula[n] == ")":
                start = stack.pop()
                end = n
                result, _ = Solution.parse_non_paranthesis(formula[start + 1 : end], 0)
                # Multiply result by number if it exists
                n += 1
                number = ""
                while n < len(formula) and formula[n].isdigit():
                    number += formula[n]
                    n += 1
                if not number:
                    number = 1
                result = result * int(number)
                formula = formula[:start] + result + formula[n:]
            else:
                n += 1

        # Parse the remaining string
        result = Solution.final_parse(formula)
        # sort the result
        result = sorted(result.items(), key=lambda x: x[0])
        # Turn the result into a string
        result_string = ""
        for key, value in result:
            result_string += key
            if value != 1:
                result_string += str(value)
        return result_string
