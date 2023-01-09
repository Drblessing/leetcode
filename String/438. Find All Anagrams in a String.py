class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 1. Check every start in s using a sliding window
        p_cnt = Counter(p)
        ans = []
        for i in range(len(s) - len(p) + 1):
            # Init
            if i == 0:
                window = Counter(s[: len(p)])
            # Slide
            else:
                window[s[i - 1]] -= 1
                window[s[i + len(p) - 1]] += 1

            # Check
            ana = True
            for letter in p_cnt:
                if letter not in window or window[letter] < p_cnt[letter]:
                    ana = False
            if ana:
                ans.append(i)

        return ans
