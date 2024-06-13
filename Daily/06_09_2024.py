def merge_sort(arr):
    """Merge sort is a divide and conquer algorithm that divides the input
    array into two halves, calls itself for the two halves, and then merges
    the two sorted halves.

    Time complexity: O(n log n)
    Space complexity: O(n)
    """

    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        # while i < len(L):
        #     arr[k] = L[i]
        #     i += 1
        #     k += 1

        # while j < len(R):
        #     arr[k] = R[j]
        #     j += 1
        #     k += 1
        # After the main merge loop
        arr[k:] = L[i:] + R[j:]


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights[:]
        merge_sort(sorted_heights)
        c = 0
        for i in range(len(sorted_heights)):
            if sorted_heights[i] != heights[i]:
                c += 1

        return c
