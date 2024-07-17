# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Search a BST for a value."""
        if not root:
            return

        def _dfs(node, val):
            if not node:
                return

            # Found it
            if node.val == val:
                return node

            # Check left or right subtree based on value
            if val < node.val:
                return _dfs(node.left, val)
            else:
                return _dfs(node.right, val)

        return _dfs(root, val)
