# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        head = pointer = ListNode()

        min_heap = []

        for l in lists:

            while l:
                heappush(min_heap, l.val)
                l = l.next

        while min_heap:
            pointer.next = ListNode(heappop(min_heap))
            pointer = pointer.next

        return head.next






