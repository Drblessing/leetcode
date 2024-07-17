from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """Calculate the level of the tree with the maximum sum of all nodes.
        Stack BFS approach."""

        max_level, max_level_sum = 0, float("-inf")
        stack = [(root, 1)]
        while stack:
            next_level_stack = []
            level_sum, level = 0, stack[0][1]
            for node, level in stack:
                level_sum += node.val
                if node.left:
                    next_level_stack.append((node.left, level + 1))
                if node.right:
                    next_level_stack.append((node.right, level + 1))
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = level
            stack = next_level_stack
        return max_level
