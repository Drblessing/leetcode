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
        # Bottom up recursive solution
        # 1. From the bottom up check itself and subtrees
        # 2. If both subtrees are true and/or itself is true we've found LCA

        # Empty node
        if not root:
            return False
        # Check subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Both have p or q
        if left and right:
            return root

        # One has p or q
        elif left or right:
            # We have the other one
            if root == p or root == q:
                return root

        # None have it
        else:
            if root == p or root == q:
                return root

            else:
                return False

        return left or right
