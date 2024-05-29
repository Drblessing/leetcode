class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # pointers
        l = 0
        r = len(numbers) - 1

        while True:

            # sum
            s = numbers[l] + numbers[r]

            if s == target:
                return l + 1, r + 1


            elif s < target:

                l += 1

            elif s > target:

                r -= 1








