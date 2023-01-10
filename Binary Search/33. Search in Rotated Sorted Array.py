class Solution:
    def search(self, nums: "List[int]", target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2

            # Pivot on right side
            if target < nums[0] < nums[mid]:  # -inf
                left = mid + 1
            # Pivot on left side
            elif target >= nums[0] > nums[mid]:  # +inf
                right = mid

            # Normal binary search
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            # Found it!
            else:
                return mid
        return -1
