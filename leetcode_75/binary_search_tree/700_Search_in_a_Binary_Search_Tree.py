class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Search a BST for a value with short-circuiting."""
        current = root

        while current:
            if current.val == val:
                return current  # Found the value
            elif val < current.val:
                current = current.left  # Go left
            else:
                current = current.right  # Go right

        return None  # Value not found
