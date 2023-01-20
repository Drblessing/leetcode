class Solution:
    def rob(self, nums: List[int]) -> int:
        # Last house is adjacent to first house
        # We need to calculate two robs,
        # 1. Rob first house, so last house is untouchable
        # 2. Don't rob first house, so everything else is normal

        # Solution
        # 1. Calculate max amount of robbing for each scenario for each houe
        # 2. Break houses without first and without last
        # 3. Amount[n] = nums[n] + max(amount[0:n-1])
        # 4. Return max

        n = len(nums)
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        # Rob first house
        first_house = nums[:-1]
        first_house_max = self.rob_one(first_house)

        # Do not rob first houe
        no_first_house = nums[1:]
        no_first_max = self.rob_one(no_first_house)
        return max(first_house_max, no_first_max)

    def rob_one(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        elif n == 2:
            return max(nums[0], nums[1])

        amounts = [nums[0], nums[1]]

        for i in range(2, n):
            amounts.append(nums[i] + max(amounts[: i - 1]))

        return max(amounts)
