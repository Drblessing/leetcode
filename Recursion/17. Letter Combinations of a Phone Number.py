class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Recursive
        # 1. Recursively call function until digits is 0
        # 2. Add each potential letter everytime

        # Degenerate Case
        if len(digits) == 0:
            return []
        # Legends
        numbers_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        combos = []

        def recursive_combos(combinations, digits_left=digits):
            # Base case
            if len(digits_left) == 0:
                combos.extend(combinations)
                return
            # Add potential letters to combinations
            current_letter = digits_left[0]
            initial_combinations = combinations
            combinations = []
            for letter in numbers_to_letters[current_letter]:
                for combo in initial_combinations:
                    new_combo = combo + letter
                    combinations.append(new_combo)
            recursive_combos(combinations, digits_left[1:])

        recursive_combos([""])
        return combos
