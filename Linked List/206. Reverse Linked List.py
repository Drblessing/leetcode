# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Iterate through nodes
        # 2. Save next nodes
        # 3. Set current node next to prev

        prev = None
        curr = head
        # Go through all the nodes
        while curr:
            # Save nodes
            tmp_save = curr.next
            # Reverse arrows
            # Set curr to prev
            curr.next = prev
            # Set prev to curr
            prev = curr
            curr = tmp_save
        return prev
