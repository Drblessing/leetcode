# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Bottom-up Recurisve solution
        # 1. Start from the bottom recurisvely
        # 2. Height of empty node is 0
        # 3. Keep track of subtrees heights
        # 4. If more than 1 apart return false

        return self.height(root) >= 0

    def height(self, root):
        if root is None:
            return 0
        left, right = self.height(root.left), self.height(root.right)
        print(root.val)
        print(left)
        print(right)
        print()
        # Check for valid subtrees and balanced subtrees
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1
