from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.index = 0
        n = len(formula)

        def parse_formula() -> defaultdict:
            atom_count = defaultdict(int)
            while self.index < n:
                if formula[self.index] == "(":
                    self.index += 1
                    nested_count = parse_formula()
                    self.index += 1  # Skip the closing parenthesis
                    multiplier = parse_number()
                    for atom, count in nested_count.items():
                        atom_count[atom] += count * multiplier
                elif formula[self.index] == ")":
                    return atom_count
                else:
                    atom = parse_atom()
                    count = parse_number()
                    atom_count[atom] += count
            return atom_count

        def parse_atom() -> str:
            start = self.index
            self.index += 1  # Move past the uppercase letter
            while self.index < n and formula[self.index].islower():
                self.index += 1
            return formula[start : self.index]

        def parse_number() -> int:
            start = self.index
            while self.index < n and formula[self.index].isdigit():
                self.index += 1
            return int(formula[start : self.index] or 1)

        final_count = parse_formula()
        sorted_atoms = sorted(final_count.items())
        result = "".join(
            f"{atom}{count if count > 1 else ''}" for atom, count in sorted_atoms
        )
        return result


print(Solution().countOfAtoms("(Mg(OH)2)2"))
