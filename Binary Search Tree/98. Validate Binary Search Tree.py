# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Recursive
        # 1. Iterate through tree
        # 2. Check each subtree with upper and lower limits

        def validateBST(root, lower_limit=-math.inf, right_limit=math.inf):
            # Empty nodes are valid
            if not root:
                return True

            # Tree must be in bounds
            elif not (lower_limit < root.val < right_limit):
                return False

            return validateBST(root.left, lower_limit, root.val) and validateBST(
                root.right, root.val, right_limit
            )

        return validateBST(root)
