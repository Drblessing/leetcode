class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        # 1. Iterate through s with a for loop
        # 2. Create the longest substring for every end letter
        # 3. If letter has never been seen before, then just the
        # len of the sliding window
        # 4. If it has been seen, check whether the letter
        # is still in the sliding window
        # 5. Update where the letter was last saw and the start of the
        # sliding window

        seen = {}
        sliding_window_l = 0
        max_length = 0
        for sliding_window_r, letter in enumerate(s):
            if letter not in seen:
                max_length = max(max_length, sliding_window_r - sliding_window_l + 1)

            else:
                # Might be outside window
                if seen[letter] < sliding_window_l:
                    max_length = max(
                        max_length, sliding_window_r - sliding_window_l + 1
                    )

                else:
                    # We only update the sliding window start
                    # if it would contain duplicates
                    sliding_window_l = seen[letter] + 1

            # Update seen
            seen[letter] = sliding_window_r
        return max_length
