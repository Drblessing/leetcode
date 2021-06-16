class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def _backtrack(S='', l=0, r=0):

            if len(S) == 2 * n: ans.append(S)

            if l < n: _backtrack(S + '(', l + 1, r)

            if r < l: _backtrack(S + ')', l, r + 1)

        _backtrack()

        return ans