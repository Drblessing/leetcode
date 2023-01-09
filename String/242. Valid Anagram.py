class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Counter s and t
        # 2. Compare counters
        # 1.
        s_cnt, t_cnt = Counter(s), Counter(t)
        # 2.
        return s_cnt == t_cnt
