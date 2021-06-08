# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = pointer = ListNode()

        while l1 and l2:

            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next

            else:
                pointer.next = l2
                l2 = l2.next

            pointer = pointer.next

        pointer.next = l1 or l2
        return head.next
