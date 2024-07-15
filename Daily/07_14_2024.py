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
        return c, n

    @staticmethod
    def parse_non_paranthesis(fomula: str, n: int):
        """Parse a string that does not contain any paranthesis."""
        result = Counter()
        while n < len(fomula):
            if Solution.is_uppercase_letter(fomula[n]):
                r, n = Solution.parse_chemical_symbol(fomula, n)
                result += r
            else:
                n += 1
        return result, n

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
        result = Counter()
        # Replace parantehsis with a string
        while n < len(formula):
            if formula[n] == "(":
                stack.append(Counter())
                n += 1
            elif formula[n] == ")":
                c = stack.pop()
                # Check if there is a number after the paranthesis
                n += 1
                numeric_string = ""
                while n < len(formula) and formula[n].isdigit():
                    numeric_string += formula[n]
                    n += 1
                if not numeric_string:
                    numeric_string = 1
                numeric_value = int(numeric_string)
                for k, v in c.items():
                    c[k] = v * numeric_value
                if stack:
                    stack[-1] += c
                else:
                    result += c

            # Must be an uppercase letter
            else:
                r, n = Solution.parse_chemical_symbol(formula, n)
                if stack:
                    stack[-1] += r
                else:
                    result += r

        # Combine all the counters
        for c in stack:
            result += c

        # Sort the result
        print(result)
        result = dict(sorted(result.items()))
        result = "".join([f"{k}{v}" if v != 1 else k for k, v in result.items()])

        return result


test_string = "Ag3((H2O)2)3"
print(Solution().countOfAtoms(test_string))
