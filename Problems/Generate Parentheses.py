class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def _backtrack(S: str = '', l: int = 0, r: int = 0) -> None:

            if len(S) == n * 2:
                ans.append(S)

            elif l < n:
                _backtrack(S + '(', l + 1, r)

            if r < l: _backtrack(S + ')', l, r + 1)

        _backtrack()

        return ans




