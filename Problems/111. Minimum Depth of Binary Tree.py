from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """Calculate the minimum depth of a binary tree
        to a leaf node, iteratively.

        We iterate from the root and append its children to the queue,
        keeping track of depth along the way, and short circuiting whenever we
        find a leaf. This is guaranteed to be the minimum depth because we iterate
        in a breadth-first manner, not depth-first.

        Time Complexity: O(n)
        Space Complexity: O(n)"""

        if root is None:
            return 0

        # Queue format: (node, depth)
        queue = deque([(root, 1)])

        while queue:
            # Pop the leftmost node from the queue
            cur_node, depth = queue.popleft()

            # Check if the node is a leaf
            if self.isLeaf(cur_node):
                return depth

            # Append its children to the queue
            if cur_node.left is not None:
                queue.append((cur_node.left, depth + 1))

            if cur_node.right is not None:
                queue.append((cur_node.right, depth + 1))

        # Shouldn't ever reach here
        return -1

    def isLeaf(self, node):
        return node.left is None and node.right is None
