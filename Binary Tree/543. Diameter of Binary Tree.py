# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS Bottom-up solution
        # 1. The max path for a node is the sum of the max subtrees paths plus 1
        # 2. Iterate through bubbling up max path

        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node):
        # Base Case
        if not node:
            return 0
        # Recursive Case
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1
