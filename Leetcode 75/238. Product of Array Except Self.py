class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Calculate the product of array except self."""

        # Initialize forward and backward product.
        forward = [nums[0]]
        backward = [nums[-1]]
        # Calculate forward product.
        for i in range(1, len(nums)):
            forward.append(forward[-1] * nums[i])
        # Calculate backward product.
        for i in range(len(nums) - 2, -1, -1):
            backward.append(backward[-1] * nums[i])
        backward = backward[::-1]
        test = 3
        # Calculate product except self
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(backward[i + 1])
            elif i == len(nums) - 1:
                result.append(forward[i - 1])
            else:
                result.append(forward[i - 1] * backward[i + 1])
        return result
