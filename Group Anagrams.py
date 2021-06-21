from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)

        for s in strs:
            s_ = ''.join(sorted(s))

            ht[s_].append(s)

        return list(ht.values())