# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Top-Down DFS
        # 1. Iterate down through roots
        # 2. Increment depth by 1
        # 3. Return max depth

        self.max_depth = 0

        def dfs(root, depth):
            if root:
                self.max_depth = max(self.max_depth, depth)
                dfs(root.left, depth + 1)
                dfs(root.right, depth + 1)

        dfs(root, 1)
        return self.max_depth
