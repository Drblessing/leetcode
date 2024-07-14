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
        return symbol, n, int(numeric_string)

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

    def countOfAtom(self, formula: str):
        """Parse the number of atoms present in a simple
        atom string, not containing any paranthesis."""
        pass

    def countOfAtoms(self, formula: str) -> str:

        return "placeholder"


test_string = "H2O"


n = 0
while n < len(test_string):
    if Solution.is_uppercase_letter(test_string[n]):
        symbol, n, number = Solution.parse_chemical_symbol(test_string, n)
        print(symbol, n, number)
    else:
        n += 1
