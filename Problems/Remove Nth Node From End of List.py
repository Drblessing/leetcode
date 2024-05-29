# A dummy node in front of the list is the best way to deal with edge cases
# we first pass through list to get length and then
# we skip over the node we want to remove
# there is a single-pass solution with two pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if head.next == None: return head.next

        # define dummy node for edgecases
        dummy = ListNode(next=head)

        # find length of list
        first = head
        l = 0
        while first != None:
            l += 1
            first = first.next

        # subtract n from length to get what node it wants us to delete

        # for example if l = 5, n = 2 -> L = 3
        l -= n

        # memory manipulation, first now edits dummy in place
        first = dummy

        # iterate until we find where we want to skip
        while l > 0:
            l -= 1
            first = first.next

        print(first.val)  # should be the node before the one we want to del (3)

        # set the next node to 2 nodes ahead, skipping the next node
        # not that this affects dummy because they are modifying the same
        # place in memory
        first.next = first.next.next

        # return dummy.next, the actual list we are looking at
        return dummy.next