# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from itertools import pairwise
from typing import List, Optional


class Solution:
    @staticmethod
    def smallest_diff_pairwise(sorted_list):
        return min(b - a for a, b in pairwise(sorted_list))

    def isCriticalPoint(self, prev, cur, next_, i):
        if (prev is None) or (cur is None) or (next_ is None):
            return -1

        prev_val, cur_val, next_val = prev.val, cur.val, next_.val

        if (prev_val < cur_val and next_val < cur_val) or (
            prev_val > cur_val and next_val > cur_val
        ):
            return i
        else:
            return -1

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """Find the minimum and maximum distance between any two distinct critical points
        in a linked list."""

        # List of positions of critical points
        critical_points = []

        # Check if head is one, two, or three nodes
        # The list must be at least four length to satisfy problem
        if (head is None) or (head.next is None) or (head.next.next is None):
            return [-1, -1]

        # Iterate through list
        prev = head
        cur = head.next
        i = 1
        while cur:
            next_ = cur.next
            # Find critical points
            point = self.isCriticalPoint(prev, cur, next_, i)
            if point != -1:
                critical_points.append(point)
            i += 1
            prev = cur
            cur = cur.next

        # Check for enough critical points
        if len(critical_points) < 2:
            return [-1, -1]

        # The list of critical points is already sorted, so now we calculate the min and max distance
        max_distance = critical_points[-1] - critical_points[0]
        min_distance = Solution.smallest_diff_pairwise(critical_points)

        return [min_distance, max_distance]
