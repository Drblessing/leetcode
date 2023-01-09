class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. Count characters in t
        # 2. Create sliding window
        # 3. Increment r to look for desirable windows
        # 4. If found start incrementing l
        # 5. Increment r until it reaches the end

        t_cnt = dict(Counter(t).items())
        # Sliding window
        window = defaultdict(int)
        l, r = 0, 0
        min_win_len = float("inf")
        min_win = ""
        temp_win = ""
        while r < len(s):
            letter = s[r]
            window[letter] += 1
            temp_win += letter
            if self.checkDesirable(window, t_cnt):
                if len(temp_win) < min_win_len:
                    min_win = temp_win
                    min_win_len = len(temp_win)

                # Iterate l while window desirable
                while self.checkDesirable(window, t_cnt):
                    if len(temp_win) < min_win_len:
                        min_win = temp_win
                        min_win_len = len(temp_win)
                    left_letter = s[l]
                    window[left_letter] -= 1
                    l += 1
                    temp_win = temp_win[1:]
            r += 1

        return min_win

    def checkDesirable(self, window, t_cnt):
        for letter in t_cnt:
            if window[letter] < t_cnt[letter]:
                return False

        return True
