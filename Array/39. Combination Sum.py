class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. Iterate through candidates in ascending order
        # 2. Perform a dfs for solutions with the smallest numbers

        combo_sums = []
        n = len(candidates)

        def _dfs(combo, combo_sum=0, idx=0):
            # Too high
            if combo_sum > target:
                return
            # Just right
            if combo_sum == target:
                combo_sums.append(combo)
                return
            # Iterate through all potential answers
            # Only add numbers that we haven't gone through yet
            # We add candidates in ascending order
            # So first candidate tried is all smallest number,
            # then second is all smallest number + second smallest number, etc.
            for i in range(idx, n):
                _dfs(combo + [candidates[i]], combo_sum + candidates[i], i)

        _dfs([])
        # Combo sums is mutated in dfs so can use it directly
        # Avoid repeat solutions by trying each combination sum once
        return combo_sums
