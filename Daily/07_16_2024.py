# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirection(self, node, val, path) -> str:
        """Get direction to a node in a tree."""

        if not node:
            return ""

        if node.val == val:
            return path

        if node.left:
            left = self.getDirection(node.left, val, path + "L")
            if left:
                return left
        if node.right:
            right = self.getDirection(node.right, val, path + "R")
            if right:
                return right

        return ""

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        return "yo"


# Create test tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


print(Solution().getDirection(root, 7, ""))  # "L"
