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
        sumNode = curNode.next

        # Iterate through the linked list
        while sumNode:
            # Create a fast pointer that iterates until we reach the next 0 
            curSum = 0 
            # Iterate until next 0 
            while sumNode.val != 0: 
                curSum += sumNode.val
                sumNode = sumNode.next
            # Set value to sum 
            curNode.val = curSum
            # Iterate to next node or end of list
            sumNode = sumNode.next
            # Set curNode next to this
            curNode.next = sumNode
            # Go to the next node
            curNode = curNode.next

        return head