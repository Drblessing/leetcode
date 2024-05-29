from collections import Counter

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        def _sort(x):
            if x in order:
                return order.index(x)

            return 0

        return ''.join(sorted(str, key=lambda x: _sort(x)))
