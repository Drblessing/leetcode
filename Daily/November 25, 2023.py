# Assuming your Solution class is defined here
class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        for i in range(1, n):
            res[0] += nums[i] - nums[0]
        for i in range(1, n):
            res[i] = (
                res[i - 1]
                + (nums[i] - nums[i - 1]) * i
                - (nums[i] - nums[i - 1]) * (n - i)
            )
        return res


# Driver Code
if __name__ == "__main__":
    # Test Case 1
    input = [2, 3, 5]
    expected = [4, 3, 5]
    actual = Solution().getSumAbsoluteDifferences(input)
    assert actual == expected
    print(actual)

    # Test Case 2
    input = [1, 4, 6, 8, 10]
    expected = [24, 15, 13, 15, 21]
    actual = Solution().getSumAbsoluteDifferences(input)
    assert actual == expected
    print(actual)
