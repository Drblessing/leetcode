# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Merge nodes between 0 on the linked list."""

        # Create a curNode that starts at the head
        curNode = head

        # Iterate through the linked list
        while curNode.next:
            # Create a fast pointer that iterates until we reach the next 0
            curSum = 0
            fast = curNode.next
            while fast.val != 0:
                curSum += fast.val
                fast = fast.next
            # Set curNode to fast after changing val
            curNode.val = curSum
            curNode.next = fast
            curNode = fast

        # Remove 0
        curNode = head
        while curNode:
            if curNode.next.val == 0:
                curNode.next = None
            curNode = curNode.next
        return head
