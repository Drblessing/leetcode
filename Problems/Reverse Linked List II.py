# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        head_ = head

        if right == left: return head

        # iterate through list
        i = 1
        reverse = []

        while head:

            if left <= i <= right: reverse.append(head.val)
            i += 1

            head = head.next

        rl = pointer = ListNode()
        while reverse:
            pointer.next = ListNode(reverse.pop())

            pointer = pointer.next

        rl = rl.next

        # iterate again inserting reversed list
        i = 1

        ans = pointer = ListNode()

        while head_:

            if i == left:
                pointer.next = rl

                for j in range(left, right + 1):
                    head_ = head_.next
                    pointer = pointer.next


            else:

                pointer.next = head_
                pointer = pointer.next
                head_ = head_.next

            i += 1

        return ans.next





