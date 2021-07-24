# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def contains_one(node: TreeNode) -> None:

            # End of the line, do not modify tree
            if node is None: return False

            # Call function on subtrees
            left = contains_one(node.left)
            right = contains_one(node.right)

            # If the subtrees do not contain a one, prune them
            if not left: node.left = None
            if not right: node.right = None

            # return 1 if val = 1 or any subtree val = 1
            return node.val or left or right

        # prune
        contains_one(root)

        # No ones in tree
        if (not root.left) and (not root.right) and (root.val == 0): root = None

        return root

