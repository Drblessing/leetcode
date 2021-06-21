from collections import Counter


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        combo_sums = []

        n = len(candidates)

        def _dfs(combo=[], combo_sum=0, idx=0):

            if combo_sum > target: return

            if combo_sum == target: combo_sums.append(combo); return

            # iterate through all potential answers
            for i in range(idx, n):
                _dfs(combo + [candidates[i]], combo_sum + candidates[i], i)

        _dfs()

        return combo_sums


