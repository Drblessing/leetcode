class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        # Triangle number problem
        ans, g, t, b, bt = 0, 0, 1, 0, 1

        for i, v in enumerate(nums):

            if v > right:

                ans += g
                ans -= b
                g, t, b, bt = 0, 1, 0, 1

            else:

                if left <= v <= right:
                    ans -= b
                    b, bt = 0, 1
                    g += t
                    t += 1

                else:
                    g += t
                    t += 1
                    b += bt
                    bt += 1
        ans += g
        ans -= b
        return ans

