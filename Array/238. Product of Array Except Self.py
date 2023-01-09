class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We need to calcule the prefix and postfix product for each
        # index i
        # 2 pass

        # Solution
        # 1. Forward pass calculating prefix product
        # 2. Backward pass calculating postfix product
        # 3. Multiply the two together

        # 1.
        n = len(nums)
        prefix_prod = [1] * n
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i - 1] * nums[i - 1]

        # 2.
        postfix_prod = [1] * n
        for i in range(n - 2, -1, -1):
            postfix_prod[i] = postfix_prod[i + 1] * nums[i + 1]

        # 3.
        ans = []
        for i in range(n):
            ans.append(prefix_prod[i] * postfix_prod[i])

        return ans
