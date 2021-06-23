from itertools import groupby

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        # groupby name and typed
        name = [(i, len(list(v))) for i, v in groupby(name)]

        typed = [(i, len(list(v))) for i, v in groupby(typed)]

        # mismatched groups
        if len(name) != len(typed): return False

        # iterate through name:
        for i, v in enumerate(name):

            # wrong letter
            if name[i][0] != typed[i][0]: return False

            # not enough letter
            if name[i][1] > typed[i][1]: return False

        return True





