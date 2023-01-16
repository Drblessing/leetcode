# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 1. Create dummy list
        # 2. Iterate adding until one list is empty
        # 3. Add remining list to the end

        head = dummy = ListNode()
        # Iterate until one list is empty
        while list1 and list2:
            # Check for next val
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        # Add remaining list
        dummy.next = list1 or list2
        return head.next
