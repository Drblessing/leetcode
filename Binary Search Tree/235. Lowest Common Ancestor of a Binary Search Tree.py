# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Iterative Solution
        # 1. Sort ancestors
        # 2. Iterate through tree looking for p and q using BST

        lo, hi = sorted([p, q], key=lambda x: x.val)
        while root:
            # LCA
            if lo.val < root.val < hi.val:
                return root
            # Search subtrees
            elif root.val > hi.val:
                root = root.left
            elif root.val < lo.val:
                root = root.right
            # Root is p or q
            else:
                return root
